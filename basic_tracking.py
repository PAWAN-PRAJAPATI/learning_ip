from collections import deque
import numpy as np
import argparse
import imutils
import cv2


camera = cv2.VideoCapture(0)
# keep looping
while True:
    # grab the current frame
    (grabbed, frame) = camera.read()
    # if we are viewing a video and we did not grab a frame,
    # then we have reached the end of the video
    # IP webcam image stream
    # URL = 'http://10.254.254.102:8080/shot.jpg'
    # urllib.urlretrieve(URL, 'shot1.jpg')
    # frame = cv2.imread('shot1.jpg')


    # resize the frame, blur it, and convert it to the HSV
    # color space
    frame = imutils.resize(frame, width=800)

    blurred = cv2.GaussianBlur(frame, (11,11), 0)
    hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)

    cv2.imshow("Frame", hsv)
    cv2.waitKey(1)
    key = cv2.waitKey(1) & 0xFF
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()