#0311-1-ClickMakeNemo.py
import numpy as np
import cv2
#첫번쨰 좌표값 버튼 다운 값을 얻어내기
#버튼 다운값을 얻어내기
#두개의 좌표값 확인해보고
#사각형 그리기 두개값을 계산해서 위드 헤이트 얻어낸 정보로
#풀 텍스트를 이용해 컨버스에 택스트입력하기



#onmouse 함수를 만들어서 event 가 마우스왼쪽버튼을 누를때 이벤트발생
#r버튼은 오른쪽버튼
def onMouse(event, x, y, flags, param):
    ##    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_SHIFTKEY:
            cv2.rectangle(param[0], (x - 5, y - 5), (x + 5, y + 5), (255, 0, 0))
        else:
            cv2.circle(param[0], (x, y), 5, (255, 0, 0), 3)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(param[0], (x, y), 5, (0, 0, 255), 3)
    elif event == cv2.EVENT_LBUTTONDBLCLK: #더블클릭시 코드 실행행        param[0] = np.zeros(param[0].shape, np.uint8) + 255
    cv2.imshow("img", param[0])


img = np.zeros((512, 512, 3), np.uint8) + 255
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse, [img])
cv2.waitKey()
cv2.destroyAllWindows()
