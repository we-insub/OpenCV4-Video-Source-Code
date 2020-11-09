#0419-subtractMinus.py
# 파일을 어둡게 만드는일 add반대연산
# 레나 귀신사진 만들기 흰색 으로변함
import cv2
import numpy as np

src1 = cv2.imread('/home/mato/data/lena.jpg', cv2.IMREAD_GRAYSCALE)
src2 = np.zeros(shape=(512,512), dtype=np.uint8)+255

dst1 = 255 - src1
dst2 = cv2.subtract(src2, src1)
dst3 = cv2.compare(dst1, dst2, cv2.CMP_NE) # cv2.CMP_EQ
n    = cv2.countNonZero(dst3)
print('n = ', n)

cv2.imshow('dst1',  dst1)
cv2.imshow('dst2',  dst2)
cv2.waitKey()    
cv2.destroyAllWindows()
