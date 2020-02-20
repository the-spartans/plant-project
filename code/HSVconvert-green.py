# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:14:20 2020

@author: Harish
"""

import cv2
import numpy as np

"cap = cv2.VideoCapture(0)"

#while(1):

    # Take each frame
frame_green = cv2.imread(r'C:\Users\Harish\Desktop\Plant project repo\plant-project\code\resize.jpg')
count_green = 0
    # Convert BGR to HSV
hsv = cv2.cvtColor(frame_green, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
lower_green = np.array([25,100,100])
upper_green = np.array([80,225,225])

    # Threshold the HSV image to get only blue colors
mask_green = cv2.inRange(hsv, lower_green, upper_green)

count_green = np.sum(mask_green == 255)

    # Bitwise-AND mask and original image
res_green = cv2.bitwise_and(frame_green,frame_green, mask= mask_green)

print(count_green)
cv2.imwrite("frame_green.jpg", frame_green)
cv2.imwrite("mask_green.jpg", mask_green)
cv2.imwrite("result_green.jpg", res_green)
cv2.imshow('frame',frame_green)
cv2.imshow('mask',mask_green)
cv2.imshow('res',res_green)
k = cv2.waitKey(5) & 0xFF
#if k == 27:
 #   break

"cv2.destroyAllWindows()"