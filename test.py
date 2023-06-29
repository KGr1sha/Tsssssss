import cv2


screen = cv2.imread('Screenshot 2023-06-29 125822.png')
button = cv2.imread('broken message.png')
result = cv2.matchTemplate(screen, button, cv2.TM_CCOEFF_NORMED)
cv2.imshow('r', result)
cv2.waitKey()