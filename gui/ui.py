#!/usr/bin/env python
from Utils import Point
import ImageProcessing as img
import TcpClient as tcp
import time
import sys
import cv2
import numpy as np

def preProcess(image):
    # Filters
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def getPattern():
    pattern = cv2.imread('Pattern.PNG')
    pattern = preProcess(pattern)
    return pattern


def findSinglePattern(img, pattern):
    found = False
    # cv2.imshow("Pattern", pattern)
    # cv2.imshow("Image", img)

    res = cv2.matchTemplate(img, pattern, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    loc = np.where(res >= threshold)

    start_point = Point(0, 0)

    if loc[0].size > 0:
        found = True
        start_point = Point(loc[1][0], loc[0][0])
        print "FOUND SOMETHING!!"

    else:
        found = False
        start_point = Point(0, 0)
        print "Pattern Not Found!"

    return found, start_point

def main():
    
    breakloop = False

    # Start Video
    cap = cv2.VideoCapture(1)
    sampleFrame = 0
    personList={}

    while (True):

        # Capture frame-by-frame
        ret, frame = cap.read()

        gray = preProcess(frame)

        sampleFrame += 1

        if sampleFrame % 1 == 0:

            cv2.imshow("Frame", gray)

            if cv2.waitKey(1) & 0xFF == ord('q') or breakloop:
                break

            if cv2.waitKey(1) & 0xFF ==q ord('a'):
                print "Pic"
                cv2.imshow("pic1", gray)
                cv2.moveWindow("pic1", 50, 50)

            if cv2.waitKey(1) & 0xFF == ord('d'):
                cv2.destroyWindow("pic1")
            # time.sleep(0.2)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return

if __name__ == '__main__':
  main()