#0413-HSV.py
import cv2
src = cv2.imread('./data/lena.jpg')
#HSV 색을 표현하는법 색상 채도 명도로 값을 표현하는것 ,
#원기둥에서 H값은 색이 빨강노랑그린파랑블루 0도에서 몇도만큼돌았냐에 따라서 색상값이 회전값으로정해짐
#S값은 원기둥 컨택정된 각도의 값을 떼서 , 얼마나 색이 선명한가
#V값은 원기둥 컨택된 각도의 값을 깊이로 따짐, 얼마나 밝은가, 어두운가
gray   = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
yCrCv = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb) #y는 밟기 신호를 갖고 데이터값조
hsv    = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

cv2.imshow('gray',  gray)
cv2.imshow('yCrCv', yCrCv)
cv2.imshow('hsv',   hsv)

cv2.waitKey()    
cv2.destroyAllWindows()
