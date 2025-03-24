'''
This code is a real-time face detection program using your computer's webcam. Here's what it does:

Key Features:
Face Detection

Uses OpenCV's pre-trained Haar Cascade classifier (haarcascade_frontalface_default.xml) to detect faces.

Converts each frame to grayscale (better for detection) and scans for faces.

Real-Time Processing

Continuously captures video from your default camera (cv2.VideoCapture(0)).

Draws a blue rectangle around detected faces.

Controls

Press 'q' to quit the program.

How It Works:
clf.detectMultiScale() checks for faces with parameters:

scaleFactor=1.1: Adjusts for different face sizes.

minNeighbors=5: Higher values reduce false detections.

minSize=(30,30): Ignores objects smaller than 30x30 pixels.

cv2.rectangle() highlights detected faces in the live video feed.

Output:
A window titled "Faces" shows the webcam feed with real-time face detection.

Note: Requires OpenCV (cv2). Install it with:
pip install opencv-python

Run it, and it’ll track faces until you press 'q'! 
'''
import pathlib
import cv2

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"

clf= cv2.CascadeClassifier(str(cascade_path))

cam= cv2.VideoCapture("video.mp4")

while True:
    _, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,
        scaleFactor= 1.1,
        minNeighbors= 5,
        minSize=(30,30),
        flags= cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x,y), (x + width, y + height), (255,255, 0), 2)

    cv2.imshow("Faces", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
