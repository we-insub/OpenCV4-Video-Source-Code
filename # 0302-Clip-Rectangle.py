#0302-Clip-Rectangle.py
import cv2
import numpy as np
#클립 라인 사각형에서 직선 두개를 점을 짓고 그 점을 이어서 직선을 만드는것

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255

x1, x2 = 100, 400
y1, y2 = 100, 400
cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255))

pt1 = 120, 50
pt2 = 300, 500
cv2.line(img, pt1, pt2, (255,0,0), 2)
#캔버스이미지에 point1이 120,50 point2가 300,500 에 직선을 BGR B=255값으로 그어라
#선두께는 2


# x_start, y_start, x_width, y_height 로 값을 보자.
imgRect = (x1, y1, x2-x1, y2-y1)
#튜플로 값을 x1=100 y1=100 x2-x1=300 y2-y1=300 두 좌표가만다는 리턴값
retval, rpt1, rpt2 = cv2.clipLine(imgRect, pt1, pt2) #imgRect = 사각형
#rpt1이 위고 rpt2가 아래입니다.
if retval:
    cv2.circle(img, rpt1, radius=5, color=(0, 255, 0), thickness=-1)
    cv2.circle(img, rpt2, radius=5, color=(0, 255, 0), thickness=-1)

#선두께 -1 이라하면 사각형 안에 선을 채워준다 = thickness-1 안을 채운다
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
