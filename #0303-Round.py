#0303-Round.py
import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
cx = img.shape[0]//2
cy = img.shape[1]//2

for r in range(200, 0, -100): #시작점 200 종점이 0
    cv2.circle(img, (cx, cy), r, color=(255, 0, 0))
    #200짜리 0짜리 - 100짜리 0을 포함하지않으니 200짜리 100짜리 하나의원

cv2.circle(img, (cx, cy), radius=50, color=(0, 0, 255), thickness=-1)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
