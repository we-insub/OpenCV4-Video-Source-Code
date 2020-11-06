#0301-Line-Rectangle.py
import cv2
import numpy as np

# 도화지에 그림을 그리려 한다.
# 흰색 도화지를 만드는것이다.
# numpy 512 5125 512라는 배열에 0으로 채워진것이 만들어지는 함수
# 모든 배열에 있는 배열 요소들을 255 로 다 바꾼것이다.
# 이미지를 읽어보면 255로 채워진 512 512 채널이 3개가 만들어진것이다.
# 그러면 결과값은 흰색 도화지가 된다.

# White 배경 생성
img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
#img = np.ones((512,512,3), np.uint8) * 255

#img = np.full((512,512,3), (255, 255, 255), dtype= np.uint8)
#1,2,3채널을 그냥 다 255,255,255로 다 채워라

#img = np.zeros((512,512, 3), np.uint8) # Black 배경
#난 흰색도화지가 싫고 검은색 도화지라면 zeros로 하면 검은 배경이 만들어짐

#좌표값 사각형

pt1 = 100, 100
pt2 = 400, 400
cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)
#rectangle 사각형 그리는것
#사각형에 point1 point2 BGR 의값 g -255 그린값 두께2

cv2.line(img, (0, 0), (500, 0), (255, 0, 0), 5)
cv2.line(img, (0, 0), (0, 500), (0,0,255), 5)
#선을 500 ,0 0,500 으로 선을 긋고 색깔 선 두께

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
