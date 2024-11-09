from flask import Flask, request, jsonify, render_template
import numpy as np
import cv2
import base64
import sqlite3
from inference_sdk import InferenceHTTPClient

app = Flask(__name__)

# Initialize the Inference SDK Client for Roboflow
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="wweQ6FzDKYe2XY0XlF3m"  # Your API key
)

# Model ID for your new model on Roboflow
MODEL_ID = "yolov8-trash-detections/6"  # Your updated model ID and version

# Initialize the database
def init_db():
    conn = sqlite3.connect('trash_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trash_counts (
            trash_type TEXT PRIMARY KEY,
            count INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Store counts in the database
def store_trash_counts(trash_counts):
    conn = sqlite3.connect('trash_data.db')
    cursor = conn.cursor()
    for trash_type, count in trash_counts.items():
        # Check if the trash_type already exists
        cursor.execute('SELECT count FROM trash_counts WHERE trash_type = ?', (trash_type,))
        row = cursor.fetchone()
        if row:
            # Update existing count
            new_count = row[0] + count
            cursor.execute('UPDATE trash_counts SET count = ? WHERE trash_type = ?', (new_count, trash_type))
        else:
            # Insert new trash_type
            cursor.execute('INSERT INTO trash_counts (trash_type, count) VALUES (?, ?)', (trash_type, count))
    conn.commit()
    conn.close()

# Object detection function using Roboflow Inference SDK
def detect_trash(image):
    # Save the image temporarily
    temp_image_path = "temp_image.jpg"
    cv2.imwrite(temp_image_path, image)

    try:
        # Perform inference using the Roboflow client with the new model ID
        result = CLIENT.infer(temp_image_path, model_id=MODEL_ID)

        # Initialize counts dictionary
        counts = {}

        # Process detections
        if 'predictions' in result:
            for prediction in result['predictions']:
                class_name = prediction['class']
                counts[class_name] = counts.get(class_name, 0) + 1

        return counts

    except Exception as e:
        # Log the error and handle gracefully
        print("Error during inference:", e)
        return {}  # Return an empty dictionary if an error occurs

@app.route('/process_frame', methods=['POST'])
def process_frame():
    data = request.json
    image_data = data.get("image")

    if not image_data:
        return jsonify({"error": "No image data provided"}), 400

    # Decode the base64 image data
    image_bytes = base64.b64decode(image_data.split(",")[1])
    np_arr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Detect trash in the image
    trash_counts = detect_trash(image)

    if trash_counts:
        # Prepare the suggestion based on waste types
        waste_types = set(trash_counts.keys())
        suggestion = "Please dispose of the following items: " + ", ".join(waste_types)
        # Prepare the trash items string with counts
        trash_type = ", ".join(f"{item_name} x{count}" for item_name, count in trash_counts.items())
    else:
        trash_type = "No identifiable trash items detected."
        suggestion = "No disposal needed."

    # Store counts in the database
    store_trash_counts(trash_counts)

    return jsonify({"trash_type": trash_type, "suggestion": suggestion})

@app.route('/get_trash_counts', methods=['GET'])
def get_trash_counts():
    conn = sqlite3.connect('trash_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT trash_type, count FROM trash_counts')
    rows = cursor.fetchall()
    conn.close()

    trash_counts = {trash_type: count for trash_type, count in rows}
    return jsonify(trash_counts)

@app.route('/')
def index():
    # Render the index.html template from the templates folder
    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
