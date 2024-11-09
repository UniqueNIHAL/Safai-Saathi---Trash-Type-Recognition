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

# Trash item IDs mapping
trash_item_ids = {
    44: "bottle",
    46: "wine glass",
    47: "cup",
    48: "fork",
    49: "knife",
    50: "spoon",
    51: "bowl",
    52: "banana",
    53: "apple",
    54: "sandwich",
    55: "orange",
    56: "broccoli",
    57: "carrot",
    58: "hot dog",
    59: "pizza",
    60: "donut",
    61: "cake",
    62: "chair",
    63: "couch",
    64: "potted plant",
    65: "bed",
    67: "dining table",
    70: "toilet",
    72: "tv",
    73: "laptop",
    74: "mouse",
    75: "remote",
    76: "keyboard",
    77: "cell phone",
    78: "microwave",
    79: "oven",
    80: "toaster",
    81: "sink",
    82: "refrigerator",
    84: "book",
    85: "clock",
    86: "vase",
    87: "scissors",
    88: "teddy bear",
    89: "hair drier",
    90: "toothbrush",
}

# Define the waste categories mapping
waste_categories = {
    "bottle": "dry",
    "wine glass": "dry",
    "cup": "dry",
    "fork": "dry",
    "knife": "dry",
    "spoon": "dry",
    "bowl": "dry",
    "banana": "wet",
    "apple": "wet",
    "sandwich": "wet",
    "orange": "wet",
    "broccoli": "wet",
    "carrot": "wet",
    "hot dog": "wet",
    "pizza": "wet",
    "donut": "wet",
    "cake": "wet",
    "chair": "dry",
    "couch": "dry",
    "potted plant": "wet",
    "bed": "dry",
    "dining table": "dry",
    "toilet": "dry",
    "tv": "e-waste",
    "laptop": "e-waste",
    "mouse": "e-waste",
    "remote": "e-waste",
    "keyboard": "e-waste",
    "cell phone": "e-waste",
    "microwave": "e-waste",
    "oven": "e-waste",
    "toaster": "e-waste",
    "sink": "e-waste",
    "refrigerator": "e-waste",
    "book": "dry",
    "clock": "e-waste",
    "vase": "dry",
    "scissors": "dry",
    "teddy bear": "dry",
    "hair drier": "e-waste",
    "toothbrush": "dry",
}

# Object detection function using COCO-SSD
def detect_trash(image):
    # Convert the image to a tensor and prepare it for model input
    input_tensor = tf.convert_to_tensor(image)
    input_tensor = input_tensor[tf.newaxis, ...]
    detections = model(input_tensor)

    # Loop through detected objects and filter for relevant trash items
    detected_trash = []

    for i in range(detections['detection_boxes'].shape[1]):
        class_id = int(detections['detection_classes'][0][i])
        score = detections['detection_scores'][0][i].numpy()

        # Check if the detected item is a trash item and has a high confidence score
        if score > 0.5 and class_id in trash_item_ids:
            item_name = trash_item_ids[class_id]
            waste_type = waste_categories.get(item_name, "unknown")
            detected_trash.append((item_name, waste_type))

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
        # Collect the waste types
        waste_types = set(waste_type for _, waste_type in trash_items)
        # Prepare the suggestion based on waste types
        suggestion = "Please dispose of in the following bins: " + ", ".join(waste_types)
        # Prepare the trash items string
        trash_type = ", ".join(item_name for item_name, _ in trash_items)
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
