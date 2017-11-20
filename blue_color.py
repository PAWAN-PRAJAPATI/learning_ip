import cv2
import numpy as np


green=np.uint8([[[0,0,255]]])
hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()
    blurred=cv2.GaussianBlur(frame,(11,11),0)


    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                cv2.THRESH_BINARY, 11, 2)

    th3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                cv2.THRESH_BINARY, 11, 2)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([50,50,50])
    upper_blue = np.array([70,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]

    cv2.drawContours(mask.copy(), cnts, -1, (0, 255, 0), 3)

    if(len(cnts)>0):
        c = max(cnts, key=cv2.contourArea)
        print(c)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    res1,z = cv2.threshold(th2,117,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


    cv2.imshow('th2', th2)
    cv2.imshow('th3', th3)
    cv2.imshow('gray',gray)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('res1', z)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break




cv2.destroyAllWindows()