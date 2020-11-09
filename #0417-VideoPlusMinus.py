#0417-VideoPlusMinus.py
# 영상의 덧셈 뺄셈
# 만약 1이라는 값의 픽셀에 100을 더하면 조금더 밝아진다. 브라이트니스.
# add연산을 하게될경우 255값을 넘어가게 되면 다시 0으로 돌아가게 된다.
# 사진이 검은색으로 보여지는곳은 255값을 넘어서 다시 0부터 시작해서 값이 증가하는 값
# + 는 산술적으로 더한것이기 떄문에 add 함수를 사용해야 한다.
# src1 + src2 를 더해서 dst1를 만드는데,
# if문을 더해서 255 보다 크다고 하면 255 시가 되게 코딩을 추가해야한다..

import cv2
import numpy as np

src1 = cv2.imread('/home/mato/data/lena.jpg', cv2.IMREAD_GRAYSCALE)
src2 = np.zeros(shape=(512,512), dtype=np.uint8) + 100

dst1 = src1 + src2
dst2 = cv2.add(src1, src2)
#dst2 = cv2.add(src1, src2, dtype = cv2.CV_8U)


cv2.imshow('dst1',  dst1)
cv2.imshow('dst2',  dst2)
cv2.waitKey()    
cv2.destroyAllWindows()
