from collections import deque
import numpy as np
import argparse
import imutils
import cv2


cap=cv2.VideoCapture(0)
lower_blue = np.array([50, 50, 50])
upper_blue = np.array([70, 255, 255])

while True:

    _,frame1=cap.read()
    frame=cv2.GaussianBlur(frame1,(11,11),0)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_blue,upper_blue)

    mask_ans,cnts,_ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_NONE)
    #cv2.drawContours(frame1,cnts, -1, (0, 255, 0), 3)

    cv2.imshow("blue",mask)
    cv2.imshow("blue_ans", mask_ans)
    cv2.imshow("Fream",frame1)
    if(len(cnts)>0):
        M=cv2.moments(cnts[0])
        if(M["m00"]!=0):
            center = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
        area=cv2.contourArea(cnts[0])

        hull = cv2.convexHull(cnts[0])
        print(hull)



    k = cv2.waitKey(1)

cv2.destroyAllWindows()



