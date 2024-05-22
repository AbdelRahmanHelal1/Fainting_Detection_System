from ultralytics import YOLO
import cv2
import numpy as np
import cvzone
import requests

# Telegram Bot Token and Chat ID
TOKEN = "TOKEN FOR YOUR BOT"

chat_id = "CHAT ID FOR YOUR BOT"

image_path = "fall_detection.jpg"

# Load the YOLOv8 model
model = YOLO("yolov8n-pose.pt")

# Open the video file
cap = cv2.VideoCapture("VID_20240416_115636.mp4")

# Dictionary to keep track of the time each detected object has been in a certain state
times = {}


def Send_Image(bot_token, chat_id, image):
    """
    Sends an image to a Telegram chat.

    Parameters:
    - bot_token: The token for the Telegram bot.
    - chat_id: The ID of the Telegram chat to send the image to.
    - image: The file path of the image to send.
    """

    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
    files = {'photo': open(image, 'rb')}
    data = {'chat_id': chat_id}
    response = requests.post(url, files=files, data=data)
    return response.json()






# Process the video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame for consistency
    frame = cv2.resize(frame, (600, 500))

    # Predict the pose using YOLO model
    result = model.predict(frame)
    boxes = result[0].boxes.xyxy.cpu().numpy().astype(int)
    keypoints = result[0].keypoints.data.cpu().numpy().astype("float")

    # Threshold to determine if an object is on the ground
    thresh = frame.shape[1] // 2 + 100

    for idd, lm in enumerate(keypoints):
        x1, y1, x2, y2 = boxes[idd]
        x2 = x2 - x1
        y2 = (y2 - y1)
        head = round(lm[5][0])
        legleft, legright = round(lm[16][0]), round(lm[15][0])

        # Detect if the person is in a fallen state
        if int(lm[16][0]) != 0 or int(lm[15][0]) != 0:
            if abs(head - legleft) > 60 and abs(head - legright) > 60 or x2 / y2 > 1:
                if idd not in times:
                    times[idd] = 0
                times[idd] += 1

                # Draw a yellow rectangle around the detected object
                cvzone.cornerRect(frame, (x1, y1, x2, y2), colorC=(0, 255, 255))

                # Calculate the elapsed time
                seconds = times[idd] // 1000
                milliseconds = times[idd] % 1000
                time_str = "{:02d}:{:02d}".format(seconds, milliseconds)
                cv2.putText(frame, time_str, (x1, y1), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)

                # If the object has been in a fallen state for more than 30 milliseconds, mark it
                if int(milliseconds) > 30:
                    cv2.putText(frame, time_str, (x1, y1), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
                    cvzone.cornerRect(frame, (x1, y1, x2, y2), colorC=(0, 0, 255))

                    # Save the image of the detected object
                    image_to_save = frame[y1:y1 + y2, x1:x1 + x2]
                    cv2.imwrite(image_path, image_to_save)

                    # Send the image if the condition is met
                    if 32 > int(milliseconds) > 30:
                        Send_Image(TOKEN, chat_id, image_path)
            else:
                # Reset the time if the object is not in a fallen state
                cvzone.cornerRect(frame, (x1, y1, x2, y2))
                times[idd] = 0

    # Display the frame
    cv2.imshow("frame", frame)
    cv2.waitKey(1)

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
