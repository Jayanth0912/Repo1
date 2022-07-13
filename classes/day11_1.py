# Over loading

# def add(a,b): # definition
#     return a+b
#
# # print(add(2,3))
# print(add(2,3))
#
# from day11 import add # Declaration
#
# print(add([3,4,5,6,7,8,9]))
#
# def add(a,b,c): # Definition
#     return a+b+c
#
# print(add(10,20,30))

#Over Riding


# def mul(a,b):
#     return a*b

# def mul(a,b,c=1):
#     return a*b*c
#
# print(mul(10,20))
# print(mul(10,20,30))


# Python program to take
# screenshots

import numpy
import numpy as np
import cv2
import pyautogui

# take screenshot using pyautogui
image = pyautogui.screenshot()

# since the pyautogui takes as a
# PIL(pillow) and in RGB we need to
# convert it to numpy array and BGR
# so we can write it to the disk
image = cv2.cvtColor(np.array(image),
          cv2.COLOR_RGB2BGR)

# writing it to the disk using opencv
cv2.imwrite("image1.png", image)
