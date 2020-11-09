#영상의 전단 변환
# 전단변환 Shear Transformation
# 층 밀림 변환 x축과 y축 방향에 대해 따로 정의
# 축이 틀어졌을때 ,
# 즉 왼쪽위 오른쪽위모서리는 맞는데
# 아래쪽 사진들이 축이 틀어졌을때 그거 땡기는거
# 사진 기울기 주는것 그 값을 m값이라 한다.


import sys
import numpy as np
import cv2


src = cv2.imread('/home/mato/Downloads/ch05/tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0.5, 0],
                [0, 1, 0]], dtype=np.float32)

h, w = src.shape[:2]
dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()