#0414-Resize.py
#사진확대와 축소 한장씩
import cv2
import numpy as np
src = cv2.imread('/home/mato/data/lena.jpg', cv2.IMREAD_GRAYSCALE)

dst = cv2.resize(src, dsize=(320, 240)) #사이즈 직접
dst2 = cv2.resize(src, dsize=(0,0), fx=1.5, fy=1.2) #비율로 변경 하기.

cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()    
cv2.destroyAllWindows()
