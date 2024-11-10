
# Safai Saathi - Trash Type Recognition

Welcome to **Safai Saathi** – your companion for cleaner, greener waste management! This project uses the power of AI to simplify waste segregation and help users make environmentally responsible choices. Safai Saathi is designed to recognize types of trash, guide proper disposal, and provide insights on waste management best practices. 

## 🌍 Project Overview

**Safai Saathi** leverages image recognition and advanced machine learning to automatically detect and categorize trash. The goal is simple yet impactful: to make waste segregation more efficient, accessible, and user-friendly. By using this bot, people can get real-time information on how to sort and dispose of waste effectively, ultimately helping reduce the burden on landfills and our planet.

### Key Features

- **Automated Trash Detection**: Instantly recognize different types of trash through images and guide users on proper disposal.
- **Waste Segregation Best Practices**: Learn the most effective ways to sort and manage waste at home or in public spaces.
- **Insights on Environmental Impact**: Understand how your actions contribute to sustainability goals and cleaner communities.

## 🏆 Project Goals

- **Promote Efficient Waste Segregation**: By helping users sort waste correctly, Safai Saathi aims to improve recycling rates and reduce contamination.
- **Raise Awareness**: Educate users on the importance of waste segregation and its impact on the environment.
- **Support Sustainable Development**: This project aligns with various UN Sustainable Development Goals (SDGs), including responsible consumption and climate action.
- **Data Collection for Good**: Collects data on trash depositted that can be used to keep count and to implement future practices.

## 📋 How It Works

The system uses a blend of computer vision and machine learning to analyze images of waste items. Here’s the basic flow:

1. **Image Capture**: Users snap a picture of the waste item with their smartphone or any camera-enabled device.
2. **Trash Detection**: The AI model identifies the item type (plastic, paper, metal, organic waste, hazardous materials, etc.).
3. **Guided Disposal**: The bot suggests the proper bin or disposal method for the item.
4. **Data Collection & Insights**: Waste patterns are recorded to help improve local waste management strategies.

## 🤖 Getting Started

### Prerequisites

- **Python 3.7+**: Make sure you have Python installed.
- **Google Cloud Account**: This project leverages Vertex AI and other Google Cloud tools.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/UniqueNIHAL/TrashRecognition.git
   cd TrashRecognition
   ```

2. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Google Cloud**

   - Make sure you have access to Google Cloud services like Vertex AI.
   - Set up your credentials as per the Google Cloud setup instructions.

4. **Run the Server**

   ```bash
   python server.py
   ```

### Usage

- **Interact with Safai Saathi**: The bot will prompt you for input – ask any waste-related question, and it’ll guide you on proper waste management practices.

## 🌱 How You Can Help

This project thrives on community involvement! Here’s how you can contribute:

1. **Spread the Word**: Let others know about Safai Saathi and the importance of waste segregation.
2. **Add Features**: Feel free to fork this repo and add more capabilities.
3. **Share Feedback**: Got ideas or suggestions? Open an issue or send a pull request!

## 🚀 Roadmap

- **Enhanced Image Recognition**: Improve AI accuracy to handle a broader range of waste items.
- **Interactive Educational Modules**: Incorporate tips on reducing, reusing, and recycling waste.
- **Global Waste Tracking**: Expand to show real-time waste trends and insights worldwide.

## 📜 License

This project is licensed under the APACHE License.

---

## Citations
1) 
@misc{
                            food-waste-ihk1f_dataset,
                            title = { food-waste Dataset },
                            type = { Open Source Dataset },
                            author = { workspace },
                            howpublished = { \url{ https://universe.roboflow.com/workspace-x0bbq/food-waste-ihk1f } },
                            url = { https://universe.roboflow.com/workspace-x0bbq/food-waste-ihk1f },
                            journal = { Roboflow Universe },
                            publisher = { Roboflow },
                            year = { 2024 },
                            month = { may },
                            note = { visited on 2024-11-10 },
                            }

2)
@misc{
                            yolov8-trash-detections_dataset,
                            title = { yolov8-trash-detections Dataset },
                            type = { Open Source Dataset },
                            author = { FYP },
                            howpublished = { \url{ https://universe.roboflow.com/fyp-bfx3h/yolov8-trash-detections } },
                            url = { https://universe.roboflow.com/fyp-bfx3h/yolov8-trash-detections },
                            journal = { Roboflow Universe },
                            publisher = { Roboflow },
                            year = { 2023 },
                            month = { dec },
                            note = { visited on 2024-11-10 },
                            }


## Thank you for joining us on this journey toward a cleaner, greener planet! Let's work together to make waste management easier and more impactful. 🌎
