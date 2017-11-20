import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame import locals
from collections import deque
import numpy as np
import argparse
import imutils
import cv2


vertices=[[0,0,0],[0,0,0],[0,0,0]]
edges=((0,1),(1,2))
cap=cv2.VideoCapture(0)
lower_blue = np.array([50, 50, 50])
upper_blue = np.array([70, 255, 255])

lower_green = np.array([97, 100, 117])
upper_green = np.array([117, 255, 255])

def line():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
def center():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    _, frame1 = cap.read()
    frame1 = imutils.resize(frame1, width=1000)
    frame = cv2.GaussianBlur(frame1, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    kernel = np.ones((9, 9), np.uint8)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.flip(mask, 1)
    mask_ans, cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                         cv2.CHAIN_APPROX_NONE)
    cv2.imshow("Mask",mask)
    if (len(cnts) > 0 ):
        M = cv2.moments(cnts[0])
        if (M["m00"] != 0):
            center_p = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            return (center_p)
        return (0,0)



def main():

    pygame.init()
    display = (1000, 1000)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(50, 1, 1, 1000)
    glTranslatef(0, 0, -700)
    while True:
        if(center()!=None):
            x,y=center()
            print(x,y)
        line()
        pygame.display.flip()
        pygame.time.wait(1)
        cv2.waitKey(1)
main()

def center():
    _, frame1 = cap.read()
    frame = cv2.GaussianBlur(frame1, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_ans, cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                         cv2.CHAIN_APPROX_NONE)
    if (len(cnts) > 0):
        M = cv2.moments(cnts[0])
        if (M["m00"] != 0):
            center_p = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            return center_p
    return (0,0)