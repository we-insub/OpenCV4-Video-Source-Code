#0415-Rotate.py
#사진 왼쪽 오른쪽 90도 변경
import cv2
src = cv2.imread('/home/mato/data/lena.jpg')

dst1 = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
dst2 = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('dst1',  dst1)
cv2.imshow('dst2',  dst2)
cv2.waitKey()    
cv2.destroyAllWindows()
