#0307-Angle-Change.py
import cv2
import numpy as np

img = np.zeros(shape=(512, 512, 3), dtype=np.uint8) + 255

x, y = 256, 256
size = 200

for angle in range(0, 90, 10):
    #0 에서 90도 사이에 9개의 앵글
    rect = ((256, 256), (size, size), angle)
    #256 256 가로세로 200짜리 사각형
    box = cv2.boxPoints(rect).astype(np.int32)
    r = np.random.randint(256) #색 상 랜 덤
    g = np.random.randint(256)
    b = np.random.randint(256)
    cv2.polylines(img, [box], True, (r, g, b), 2)
    #폴리라인으로 만든다

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
