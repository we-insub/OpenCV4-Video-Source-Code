#0416-GetRotate.py
#왼쪽 오른쪽 꺽기 45도씩
import cv2
src = cv2.imread('/home/mato/data/lena.jpg')

rows, cols, channels = src.shape
M1 = cv2.getRotationMatrix2D( (rows/2, cols/2),  45, 0.5 ) #로테이트를 위한 마스크 생성 중심좌표.
M2 = cv2.getRotationMatrix2D( (rows/2, cols/2), -45, 1.0 )
#중심좌표 중심좌표 각도 스케일

dst1 = cv2.warpAffine( src, M1, (rows, cols))
dst2 = cv2.warpAffine( src, M2, (rows, cols))

cv2.imshow('dst1',  dst1)
cv2.imshow('dst2',  dst2)
cv2.waitKey()    
cv2.destroyAllWindows()
