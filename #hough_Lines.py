import sys
import numpy as np
import cv2



src = cv2.imread('/home/mato/Downloads/ch06/building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

edges = cv2.Canny(src, 50, 150)
# 엣지를 houghline 에 집어넣는다
# lower 값은 1 이고 pi값은 3.14 / 180 을 해서 그 값을 집어넣고,
# 쓰레숄드 값은 160을 썻고 미니멈라인랭스 50 50보다 선에길이가 작으면 표현을 하지않는다.
# 맥시멈 라인갭은 라인끼리 거리가 가장 먼게 5 픽셀이라는 이야기이다.

lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 160,
                        minLineLength=50, maxLineGap=5)

dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1])  # 시작점 좌표
        pt2 = (lines[i][0][2], lines[i][0][3])  # 끝점 좌표
        cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()