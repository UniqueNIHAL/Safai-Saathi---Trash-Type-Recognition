from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import cv2
import base64
import io

app = Flask(__name__)

# Load the COCO-SSD model from TensorFlow Hub
model = hub.load("https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2")

# Object detection function using COCO-SSD
def detect_trash(image):
    # Convert the image to a tensor and prepare it for model input
    input_tensor = tf.convert_to_tensor(image)
    input_tensor = input_tensor[tf.newaxis, ...]
    detections = model(input_tensor)

    # Filter detections for common trash items like 'bottle', 'cup', etc.
    detected_trash = []
    trash_item_ids = {
        44: "bottle",
        47: "cup",
        49: "plate",
        50: "spoon",  # Add more IDs as needed
        52: "fork",
    }

    # Loop through detected objects and filter for relevant trash items
    for i in range(detections['detection_boxes'].shape[1]):
        class_id = int(detections['detection_classes'][0][i])
        score = detections['detection_scores'][0][i].numpy()

        # Check if the detected item is a trash item and has a high confidence score
        if score > 0.5 and class_id in trash_item_ids:
            detected_trash.append(trash_item_ids[class_id])
    
    return detected_trash

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
    trash_items = detect_trash(image)

    if trash_items:
        trash_type = ", ".join(trash_items)
        suggestion = "Please dispose of in the appropriate bin."
    else:
        trash_type = "No identifiable trash items detected."
        suggestion = "No disposal needed."

    return jsonify({"trash_type": trash_type, "suggestion": suggestion})

@app.route('/')
def index():
    # Render the index.html template from the templates folder
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
