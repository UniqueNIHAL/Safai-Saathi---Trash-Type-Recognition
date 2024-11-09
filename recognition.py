import matplotlib.pyplot as plt
import numpy as np
import cv2
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import requests

# Initialize Vertex AI
def initialize_vertex_ai(project_id: str, location: str):
    vertexai.init(project=project_id, location=location)
    multimodal_model = GenerativeModel("gemini-1.0-pro-vision")
    return multimodal_model

# Capture frames and analyze trash
def capture_and_detect(multimodal_model, api_url, frame_interval=5):
    cap = cv2.VideoCapture(0)
    frame_count = 0

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Process every nth frame
            if frame_count % frame_interval == 0:
                ret, buffer = cv2.imencode('.jpg', frame)
                image_bytes = buffer.tobytes()

                # Send to Vertex AI
                response = multimodal_model.generate_content(
                    [Part.from_bytes(content=image_bytes, mime_type="image/jpeg"), "What is shown in this image?"]
                )
                trash_type = response.text

                # Display suggestion on-screen
                if "plastic" in trash_type:
                    bin_suggestion = "Use the PLASTIC bin"
                elif "food" in trash_type:
                    bin_suggestion = "Use the ORGANIC bin"
                else:
                    bin_suggestion = "General WASTE bin"

                print("Trash Type Detected:", trash_type, "| Suggestion:", bin_suggestion)
                cv2.putText(frame, bin_suggestion, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                # Send data to backend
                data = {'trash_type': trash_type}
                requests.post(api_url, json=data)

            # Display the frame using matplotlib
            plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            plt.title('Real-time Trash Recognition')
            plt.axis('off')
            plt.show(block=False)
            plt.pause(0.01)  # Pause to allow the frame to render
            plt.clf()  # Clear the plot for the next frame

            frame_count += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        plt.close()  # Close the matplotlib window

# Variables
project_id = "hackthisfall2024-nihal"
location = "us-central1"
api_url = "http://127.0.0.1:5000/store_trash_data"

# Run the process
model = initialize_vertex_ai(project_id, location)
capture_and_detect(model, api_url)
