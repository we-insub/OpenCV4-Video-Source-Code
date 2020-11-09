import sys
import numpy as np
import cv2

def onChange(pos): # 트랙바 핸들러
    global img
    Low_TH = cv2.getTrackbarPos('Low_TH','dst')
    High_TH = cv2.getTrackbarPos('High_TH','dst')
    dst = cv2.Canny(src, 50, 150)

    cv2.imshow('img', img)


src = cv2.imread('/home/mato/Downloads/ch06/building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()


#windows 생성
cv2.setWindowTitle('dst','dst')
#window name = est

# 트랙바 생성
cv2.createTrackbar('Low_TH', 'dst', 0, 255, onChange) #track bar name
cv2.createTrackbar('High_TH', 'dst', 0, 255, onChange) # windows name
cv2.createTrackbar('Low_TH', 'dst', 50)
cv2.createTrackbar('High_TH', 'dst', 150)
dst = cv2.Canny(src, 50, 150)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()