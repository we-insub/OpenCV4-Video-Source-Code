#0421-setRNGSeed.py
# 흰 캔버스에 빨간 점들이 생겼음
# 노이즈를 이미지에 추가한다음에. 원본이미지에 노이즈가 있을때 어떻게 처리할수 있는가?
# 라는것이다.
# 랜덤 시드값을 집어넣어서 랜덤하게 점을 찍게 만들어놓고,
import cv2
import numpy as np
import time

dst = np.full((512,512,3), (255, 255, 255), dtype= np.uint8)
nPoints = 100
pts = np.zeros((1, nPoints, 2), dtype=np.uint16)

cv2.setRNGSeed(int(time.time())) # 타임.타임 년월일시분초 시간이1초지나갈때마다 점찍힐위치변경
#항상 돌때 일정하게 하고싶다면, 랜덤시드값에 특정한 문자열이나 숫자열값을 집어넣으면 된다.
#랜덤은 랜덤이지만 항상 동일한 결과가 나온다.
cv2.randu(pts, (0, 0), (512, 512))
            
# draw points
for k in range(nPoints):
    x, y = pts[0, k][:] # pts[0, k, :]
    cv2.circle(dst,(x,y),radius=5,color=(0,0,255),thickness=-1)
    #점을 랜덤포인트 찍어내게하는것
    
cv2.imshow('dst',  dst)
cv2.waitKey()    
cv2.destroyAllWindows()
