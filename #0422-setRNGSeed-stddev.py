#0422-setRNGSeed-stddev.py
# 0421 처럼 빨간점들이 나오지만 빨간점들을 확대?
# 그게 아니라면 가운데에 빨간점들을 해놓고 그 주변은 하얀색으로 아마 포인트 좌표지정
# 범위를 지정해서
import cv2
import numpy as np
import time

dst = np.full((512,512,3), (255, 255, 255), dtype= np.uint8)
nPoints = 100
pts = np.zeros((1, nPoints, 2), dtype=np.uint16)

cv2.setRNGSeed(int(time.time()))
cv2.randn(pts, mean=(256, 256), stddev=(50, 50))
#                   평균값        분산
# 랜덤하게 점을 찍어주는데, 가운데에서 점을 찍어주면 256,256 평균값의 수치이다.
# 그러니 그 주변으로 점을 기준으로분산률이 픽셀이 50,50 이 되게끔 점을 찍는다.
# 분산률을 100 , 200으로 변경한다면 더 벌어져서 점이 찍힌다.
            
# draw points
for k in range(nPoints):
    x, y = pts[0][k, :] # pts[0, k, :]
    cv2.circle(dst,(x,y),radius=5,color=(0,0,255),thickness=-1)
    
cv2.imshow('dst', dst)                
cv2.waitKey()    
cv2.destroyAllWindows()
