#0423-transpose-calcCovarMatrix.py
# 무슨 값들이 나오는데 이건 수업시간에 받아적자.
# 여태까지 배운이미지들은 돌리고 사이지를 줄이고늘리고
# transpose 라는것은 사진을 눕히거나, 사진을 3 차원 평면을두고 연산을 처리하는것을 말한다.
# ex) 사진이나 영상에서 영상시야가 누워있는것을 정면에서 바라보는것처럼 수정을 한다.
# calcCovarMatrix 를 통해 영상 처리를 하면된다.
# 가로 또는 세로 방향으로 영상을 특정 크기만큼 이동시키는 변환
# x축과 y축 방향으로의 이동 변위를 지정

import cv2
import numpy as np

X = np.array([[0, 0,  0,100,100,150, -100,-150],
              [0,50,-50,  0, 30,100,  -20,-100]], dtype=np.float64)
X = X.transpose() # X = X.T

cov, mean = cv2.calcCovarMatrix(X, mean=None, 
                               flags = cv2.COVAR_NORMAL + cv2.COVAR_ROWS)
print('mean=', mean)
print('cov=', cov)

ret, icov = cv2.invert(cov)
print('icov=',icov)

v1 = np.array([[0],[0]] , dtype=np.float64)
v2 = np.array([[0],[50]], dtype=np.float64)

dist = cv2.Mahalanobis(v1, v2, icov)
print('dist = ', dist)
                
cv2.waitKey()    
cv2.destroyAllWindows()
