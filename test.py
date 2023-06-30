import cv2
import pyautogui
from time import sleep



sleep(5)
s = pyautogui.screenshot('test_sh.png')
s = cv2.imread('test_sh.png')
cv2.imshow('s', s)
cv2.waitKey()



