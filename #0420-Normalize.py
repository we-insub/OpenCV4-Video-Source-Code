#0420-Normalize.py
# nomalize 란 정규화 하다 라는 뜻인데.
# 숫자의 범위가 0 에서 20사이에서 집에 연식 0에서 100사이 있는데
# 특정한 바운더리 안으로 숫자를 집어넣어 버린다. 스케일링에다가 집어넣는다.
# 전체 적인 전체 범위분포를 분포를 정확하게 함
# 노말라이즈로 평점 데이터를 이용할수 있다.
# ex )넷플릭스 a=7점 b=9점 c=10점
# ex ) 네이버    3점  5점    2점
# 두개의 데이터를 같이 쓰기위해선 넷플릭스는 10점 만점 네이버는 5점만점, 기준이 서로 다르다
# 평준화하기위해선 네이버에곱하기 2를 해야핮만 범위의 숫자가 다르기때문에 두개의 숫자를 섞어 쓰려면
# 같은 기준으로 바꿔야한다. 0에서 1.0사이로 변경을 하는것이다.
# 그렇다면 넷플 0.7 0.9 1.0 네이버 0.6 1.0 0.4 가 되는것이다
# 전체를 전체 평균을 1.0으로 두는 것이 정규화
# 회색에 사진질감 종이 로그린것 처럼 나옴
# 픽셀값이 0 - 255 사이인데 . 픽셀은 0-1에서하면 사진이 너무어두우니까 볼수없으니 100~200사위범위로
# 노말라이즈 한다
# 측정값을 찍어보면 100~200픽셀값을 줄일수있다.

import cv2
import numpy as np

src = cv2.imread('/home/mato/data/lena.jpg', cv2.IMREAD_GRAYSCALE)

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(src)
print('src:', minVal, maxVal, minLoc, maxLoc)

dst = cv2.normalize(src, None, 100, 200, cv2.NORM_MINMAX)
#print(sdt) #픽셀값을 100~200으로 줄인다.
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(dst)
print('dst:', minVal, maxVal, minLoc, maxLoc)

cv2.imshow('dst',  dst)
cv2.waitKey()    
cv2.destroyAllWindows()
