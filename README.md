# 🧠 Fall Detection System using YOLOv8 Pose Estimation

This project implements an **AI-powered fall detection system** using the **YOLOv8 pose model** to analyze human posture and detect if a person has fallen. When a fall is detected, the system automatically **sends an alert image via Telegram**.

![YOLOv8](https://img.shields.io/badge/YOLOv8-Pose-green)
![Alert System](https://img.shields.io/badge/Telegram-Alert-blue)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)

---

## 🎯 Features

- ✅ Real-time fall detection using YOLOv8 pose estimation
- ✅ Sends alert image to a **Telegram bot** if a fall is detected
- ✅ Highlights fall with red bounding box, normal detection with yellow
- ✅ Adjustable sensitivity and detection duration
- ✅ Lightweight model optimized for performance

---

## 📸 Demo

> Sample video frame when a fall is detected:

https://www.linkedin.com/posts/abdelrahman-helal-3630a4259_abrfaintingabrdetectionabrsystem-yolov8-opencv-activity-7199098820478091266-vbu9?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD-NFvsBIU1t34SXovuPgVPIE9z-xeVI1fY

---

## 🧠 Model

- `yolov8n-pose.pt`: A lightweight pose estimation model from [Ultralytics](https://github.com/ultralytics/ultralytics)
- Detects 17 keypoints (head, shoulders, hips, knees, etc.)

---

## 📁 Project Structure

fall_detection_project/

├── fall_detection.py # Main script

├── fall_detection.jpg # Captured alert image

├── requirements.txt # Required Python packages

├── README.md # Project documentation

└── VID_20240416_115636.mp4 # Sample video input

---

## 📦 Installation

###  Clone the repository

```bash
git clone https://github.com/AbdelRahmanHelal1/Fainting_Detection_System.git
cd fall-detection-yolov8


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

#  Install dependencies
pip install -r requirements.txt


#🛠️ How to Use
1. Update Telegram Bot Credentials
In fall_detection.py, replace the placeholders with your actual bot token and chat ID

# You can get these from @BotFather and your Telegram account.

TOKEN = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"

#  Run the script

python fall_detection.py

