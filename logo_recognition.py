#템플릿 매칭 ? 딥러닝 모델 ?
import cv2 as cv
import numpy as np 
import pyautogui

cv.namedWindow("result")
cv.moveWindow("result", 0, 500)

#캡쳐와 보여주는 것 반복
while 1:
    #캡쳐할 영역 지정 / 캡쳐한 이미지 가져옴
    pic = pyautogui.screenshot(region=(0, 0, 1900, 40))
    img_frame = np.array(pic)
    img_frame = cv.cvtColor(img_frame, cv.COLOR_RGB2BGR)

    #로고만 가져오기 위해 가우시간 블러 적용
    blur = cv.GaussianBlur(img_frame, ksize=(9, 9), sigmaX=0)
    ret, thresh1 = cv.threshold(blur, 127, 255, cv.THRESH_BINARY)

    #edge 검출
    edged = cv.Canny(blur, 10, 250)
    cv.imshow('Edged', edged)
    cv.moveWindow("Edged", 0, 100)
    """cv.waitKey(0)
    key = cv.waitKey(1)
    if key == 27:
        break"""

    #edge 이미지로 closed 찾음
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
    closed = cv.morphologyEx(edged, cv.MORPH_CLOSE, kernel)
    cv.imshow('closed', closed)
    cv.moveWindow("closed", 0, 200)
    """cv.waitKey(0)
    key = cv.waitKey(1)
    if key == 27:
        break"""

    #컨투어 경계 찾는다
    contours, _ = cv.findContours(closed.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    total = 0

    # 외곽선 그리는 용도
    # 이 코드 적용하면 원래 이미지에 초록색 선 생김
    contours_image = cv.drawContours(img_frame, contours, -1, (0, 255, 0), 1)
    cv.imshow('contours_image', contours_image)
    cv.moveWindow("contours_image", 0, 300)
    """cv.waitKey(0)
    cv.destroyAllWindows()"""

    contours_xy = np.array(contours)
    contours_xy.shape
    print(len(contours_xy))

    x_min = []
    x_max = []
    value = list()
    for i in range(len(contours_xy)):
        value = []
        tmp_x_min, tmp_x_max = 0, 0
        for j in range(len(contours_xy[i])):
            value.append(contours_xy[i][j][0][0])
            tmp_x_min = min(value)
            tmp_x_max = max(value)
        x_min.append(tmp_x_min)
        x_max.append(tmp_x_max)

    print(x_min)
    print(x_max)

    y_min = []
    y_max = []
    value = list()
    for i in range(len(contours_xy)):
        value = []
        tmp_y_min, tmp_y_max = 0, 0
        for j in range(len(contours_xy[i])):
            value.append(contours_xy[i][j][0][1])  # 네번째 괄호가 0일때 x의 값
            tmp_y_min = min(value)
            tmp_y_max = max(value)
        y_min.append(tmp_y_min)
        y_max.append(tmp_y_max)

    print(y_min)
    print(y_max)

    # image trim 하기
    result_img = []
    for i in range(len(contours_xy)):

        x = x_min[i]
        y = y_min[i]
        w = x_max[i] - x_min[i]
        h = y_max[i] - y_min[i]

        img_trim = img_frame[y:y + h, x:x + w]
        cv.imwrite('org_trim.jpg', img_trim)
        org_image = cv.imread('org_trim.jpg')

        cv.imshow('org_image', org_image)
        cv.waitKey(0)
        cv.destroyAllWindows()



    cv.imshow('result', img_frame)

    key = cv.waitKey(1)
    if key == 27:
        break