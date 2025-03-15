from flask import Flask, request, jsonify, render_template
import numpy as np
import cv2
import base64
import sqlite3
from inference_sdk import InferenceHTTPClient

app = Flask(__name__)

# Initialize the Inference SDK Client for Roboflow
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com/",
    api_key="y0QneCYytfLY0KSVZxEA"  # Your API key
)

# Model IDs for your models on Roboflow
MODEL_ID_1 = "yolov8-trash-detections/6"  # Trash detection model
MODEL_ID_2 = "food-waste-ihk1f/2"  # Food waste detection model

BIN_MAPPING = {
    'Bread': 'Food waste bin',
    'Egg': 'Food waste bin',
    'Orange': 'Food waste bin',
    'Other waste bin': 'Other waste bin',
    'Pear': 'Food waste bin',
    'Recyclable bin': 'Recyclable bin',
    'cabbage': 'Food waste bin',
    'can': 'Recyclable bin',
    'cardboard': 'Recyclable bin',
    'drink carton': 'Recyclable bin',
    'paper': 'Recyclable bin',
    'plastic bag': 'Recyclable bin',
    'plastic bottle': 'Recyclable bin',
    'plastic bottle cap': 'Recyclable bin',
    'pop tab': 'Recyclable bin',
    'potato': 'Food waste bin'
    # Add other items as needed
}


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

    counts = {}

    try:
        # Perform inference using the first model (general trash)
        result1 = CLIENT.infer(temp_image_path, model_id=MODEL_ID_1)

        # Process detections from the first model
        if 'predictions' in result1:
            for prediction in result1['predictions']:
                class_name = prediction['class']
                counts[class_name] = counts.get(class_name, 0) + 1

    except Exception as e:
        print("Error during inference with model 1:", e)

    try:
        # Perform inference using the second model (food waste)
        result2 = CLIENT.infer(temp_image_path, model_id=MODEL_ID_2)

        # Process detections from the second model
        if 'predictions' in result2:
            for prediction in result2['predictions']:
                class_name = prediction['class']
                counts[class_name] = counts.get(class_name, 0) + 1

    except Exception as e:
        print("Error during inference with model 2:", e)

    return counts

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
        # Map detected trash types to bin types and aggregate counts
        bin_types_counts = {}
        item_suggestions = []

        for trash_type, count in trash_counts.items():
            bin_type = BIN_MAPPING.get(trash_type, 'Other waste bin')  # Default to 'Other waste bin' if not found
            bin_types_counts[bin_type] = bin_types_counts.get(bin_type, 0) + count
            item_suggestions.append(f"{trash_type} (Bin: {bin_type})")

        # Prepare the suggestion based on bin types
        item_suggestions_str = ", ".join(item_suggestions)
        suggestion = "Detected items: " + item_suggestions_str

        # For display purposes, list the bins detected
        bins_detected = item_suggestions_str
    else:
        bins_detected = "No identifiable trash items detected."
        suggestion = "No disposal needed."

    # Store counts in the database
    store_trash_counts(trash_counts)

    return jsonify({"bins_detected": bins_detected, "suggestion": suggestion})

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
