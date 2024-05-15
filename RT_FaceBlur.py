"""MAIN PROGRAM - Real-time face blurring algorithm"""

import cv2
import keyboard
import time
import datetime
from DataBase_Generator import generate_data
from Login_System import login
from Logging_System import log_data


# Function to resize an image.
def resize(image, new_width=500):
    height, width, _ = image.shape
    ratio = height/width
    new_height = int(ratio*new_width)

    return cv2.resize(image, (new_width, new_height))


# Generate the user dataFrame.
user_data = generate_data()
# Run the login system and save the ID and clearance of the connected user.
user_ID, clearance = login(user_data)

# Get current (login) time for the log file.
loginTime = datetime.datetime.now()
# Declare timestamp as an empty list.
timestamp = []

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

# Video capture from webcam.
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Check if the camera opened successfully.
if not capture.isOpened():
    print("Error, feed not found.")

# Loop to examine frame by frame.
while True:

    # Read all the frames.
    _, frame = capture.read()

    # Resize the frame
    frame = resize(frame)

    # Face detections using cascade function detectMultiScale.
    detections = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=6)

    # Loop for each face in our capture.
    for face in detections:
        # Unpacking each face to the variables x, y, width, height.
        x, y, width, height = face

        # Blurring using GaussianBlur from OpenCV.
        source = frame[y:y+height, x:x+width]
        frame[y:y+height, x:x+width] = cv2.GaussianBlur(source, (91, 91), 0)

        # Draw a boundary box around the face.
        cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 0, 255), 1)

        # Display the result.
        cv2.imshow("output", frame)

        if cv2.waitKey(1) == 27:
            break

    # Lift the blurring algorithm at the press of the button depending on clearance.
    if keyboard.is_pressed("-") and clearance == "clearance 1":

        # Timer start.
        start = time.time()

        # Get current (blur lift timestamp) time for the log file.
        timestamp.append(datetime.datetime.now())

        while True:

            _, frame = capture.read()

            frame = resize(frame)

            detections = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=6)

            cv2.imshow("output", frame)

            if cv2.waitKey(1) == 27:
                break

            # If 30 seconds have passed break from the loop and blur the feed.
            if time.time() - start >= 30:
                break

            if keyboard.is_pressed("`"):
                break

    # Lift the blurring algorithm at the press of the button depending on clearance.
    if keyboard.is_pressed("-") and clearance == "clearance 2":

        # Get current (blur lift timestamp) time for the log file.
        timestamp.append(datetime.datetime.now())

        while True:

            _, frame = capture.read()

            frame = resize(frame)

            detections = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=6)

            cv2.imshow("output", frame)

            if cv2.waitKey(1) == 27:
                break

            if keyboard.is_pressed("`"):
                break

    # Close the window if "`" is pressed.
    if keyboard.is_pressed("`"):
        break


# Get current (logout) time for the log file.
logoutTime = datetime.datetime.now()
# Add information to the logfile.
log_data(user_ID, loginTime, logoutTime, timestamp, clearance)

# Releasing the feed.
capture.release()
cv2.destroyAllWindows()
