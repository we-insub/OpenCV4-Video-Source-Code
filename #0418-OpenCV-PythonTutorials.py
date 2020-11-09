#0418-OpenCV-Python Tutorials 참조
# 레나사진에 opencv 로고 박기 로고박은곳 확대사진
# 컬러 흰색 검은색 로고 화면
# 레나이미지에 src2이미지 집어넣는것 합성
# 흰색 배경은 필요없고 opencv로고를 넣기 위해 빨 초 블루 칼라 채널 RGB채널값이 들어가는지 확인하기
# 영상처리를 할때 bitwise 연산자가 중요하다
# and 연산자 를 쓸때 0 and 1 이라고 표현을 한다면,
# 니가 누군가를 데리고온다면 내가 너를 초대할께 같은 조건이다.
# 0과 1이라는 조건이 참이되야한다면, 두개가 1이되야 참이되고 그렇지 않은것은 다 거짓이된다
# roi 가 원본이미지인데, 원본이미지 중에 (워터마크 박힐곳의 원본이미지)
# bitwise_add 연산자는 둘다 0 이 아닌경우만 값을 통과시킴.
# 즉 마스크가 검정색이 아닌 경우에만 통과한다. 검은색을 제외한것은 모두 제거됨
# 즉 워터마크의 엣지가 검은색으로 만드는것이 bitwise_add 이며,
# 검은색 부분에 원본이미지를 만들기위해서는 검은색 흰색으로 붙어있는 이미지에
# bitwise_and 로 통해서 흰색영역을 통과시켜야하니까 원본이랑 합치면 흰색부분에 원본 엣지가 들어가서
# 들어간다.


import cv2
import numpy as np

src1 = cv2.imread('/home/mato/data/lena.jpg') #레나이미지.
src2 = cv2.imread('/home/mato/data/OpenCV_Logo_with_text.png') # src2는 빨 초 블루 동그라미
cv2.imshow('src2',  src2)



#1
rows,cols,channels = src2.shape
roi = src1[0:rows, 0:cols]
# 로우 콜로 채널정보를 가지고와서
# 소스원에 roi 라고 로우와 콜로를 선언한다.
# src1에 전체영역을 roi를 지정영역을 했다.
# 레나 이미지에 워터마크 박는곳에 roi 영역을 잡았다.

#2
gray = cv2.cvtColor(src2,cv2.COLOR_BGR2GRAY)
# BGR 에서 그레이로 만든다.
ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
# 마스크를 만든다.
mask_inv = cv2.bitwise_not(mask)
# 두개의 연산은 bitwise_not 이라는 연산을 하게된다
# 그렇게 되면 반전이 일어남. 실제로 오리고자 하는 영역이 흰색영역이고
# 사용하지 않는 영역을 검은색으로 만든다.
# 흰색영역은 통과하고 검은색 영역은 통과하지 못하게 하는 것.
cv2.imshow('mask',  mask)
cv2.imshow('mask_inv',  mask_inv)

#3
src1_bg = cv2.bitwise_and(roi, roi, mask = mask)
cv2.imshow('src1_bg',  src1_bg)
# 두개 값을 and를 하는데. src1_bg = 레나 사진에 검은색 마크가 박힘
# 레나에 opencv들어갈 roi영역을 비트연산으로 표시해서 그 부분을 삭제함


#4
src2_fg = cv2.bitwise_and(src2, src2, mask = mask_inv)
cv2.imshow('src2_fg',  src2_fg)

#5
##dst = cv2.add(src1_bg, src2_fg)
dst = cv2.bitwise_or(src1_bg, src2_fg)
cv2.imshow('dst',  dst)
# bitwise_or 로 하게되면 이제 원하는 워터마크와 원본사진이 합성이 됨

#6
src1[0:rows, 0:cols] = dst

cv2.imshow('result',src1)
cv2.waitKey(0)
cv2.destroyAllWindows()
