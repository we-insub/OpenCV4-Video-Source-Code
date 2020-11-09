import sys
import numpy as np
import cv2


src = cv2.imread('/home/mato/Downloads/333.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

w, h = 720, 400 #이미지 사이즈.
srcQuad = np.array([[325, 307], [760, 369], [718, 611], [231, 515]], np.float32)
# 좌표값은 임의적으로 준것이다. 사진에 명함 꼭지점에 x,y좌표값을 얻어내서 입력한 것
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)
# w,h 를 720에 400으로 잡는다 좌표순서가 0 1 그다음오른쪽아래 3 시계방향으로 좌표값 넣어주는것
# 각각의좌표를 바꿔서 넣어줬다.

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (w, h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()