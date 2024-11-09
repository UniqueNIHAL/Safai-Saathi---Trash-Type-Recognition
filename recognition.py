import cv2
import requests
import time

# Variables
api_url = "http://127.0.0.1:5000/process_frame"

def capture_and_send_frame():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot access the camera.")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Encode frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            image_bytes = buffer.tobytes()
            image_data = 'data:image/jpeg;base64,' + base64.b64encode(image_bytes).decode('utf-8')

            # Send frame to server
            response = requests.post(api_url, json={'image': image_data})
            result = response.json()

            print("Detected:", result.get('trash_type'))
            print("Suggestion:", result.get('suggestion'))
            print("-" * 50)

            time.sleep(2)  # Wait for 2 seconds before capturing the next frame
    finally:
        cap.release()

if __name__ == '__main__':
    capture_and_send_frame()
