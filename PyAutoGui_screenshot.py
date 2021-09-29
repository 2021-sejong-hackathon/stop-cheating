import cv2
import numpy as np
import pyautogui
import matplotlib.pylab as plt

cv2.namedWindow("result")
cv2.moveWindow("result", 0, 800)

#캡쳐와 보여주는 것 반복
while 1:
    #캡쳐할 영역 지정 / 캡쳐한 이미지 가져옴
    pic = pyautogui.screenshot(region=(0, 0, 1900, 40))
    img_frame = np.array(pic)
    img_frame = cv2.cvtColor(img_frame, cv2.COLOR_RGB2BGR)

    # 로고만 가져오기 위해 가우시간 블러 적용
    blur = cv2.GaussianBlur(img_frame, ksize=(9, 9), sigmaX=0)
    ret, thresh1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

    # edge 검출
    edged = cv2.Canny(blur, 10, 250)

    # edge 이미지로 closed 찾음
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

    # 컨투어 경계 찾기
    contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    total = 0

    #contours_image = cv2.drawContours(img_frame, contours, -1, (0, 255, 0), 2)

    # 검출한 로고 개수 출력
    contours_xy = np.array(contours)
    contours_xy.shape
    print(len(contours_xy))

    # x의 min, max 찾기
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
    # y의 min, max 찾기
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

    # image trim 하기
    img1 = cv2.imread('sejong.jpg')
    img2 = cv2.imread('google.jpg')
    img3 = cv2.imread('blackboard.jpg')
    for i in range(len(contours_xy)):

        if i == 0:
            print('_______첫 번째 로고 이미지_______')
        elif i == 1:
            print('_______두 번째 로고 이미지_______')
        elif i == 2:
            print('_______세 번째 로고 이미지_______')
        elif i == 3:
            print('_______네 번째 로고 이미지_______')
        elif i == 4:
            print('_______다섯 번째 로고 이미지_______')


        # 자르려고
        x = x_min[i]
        y = y_min[i]
        w = x_max[i] - x_min[i]
        h = y_max[i] - y_min[i]

        # 로고 이미지 잘라서 저장
        img_trim = img_frame[y:y + h, x:x + w]
        cv2.imwrite('org_trim.jpg', img_trim)
        org_image = cv2.imread('org_trim.jpg')
        cv2.imshow('org_trim.jpg', org_image)
        cv2.moveWindow('org_trim.jpg', 0, 500)
        key = cv2.waitKey(1)
        if key == 'q':
            break




        # 여기서부터는 히스토그램 계산 으로 이미지 유사도 평가하기 위함
        imgs = [org_image, img1, img2, img3]

        hists = []
        for j, img in enumerate(imgs):
            plt.subplot(1, len(imgs), j + 1)
            plt.title('img%d' % (j + 1))
            plt.axis('off')
            plt.imshow(img[:, :, ::-1])
            # ---① 각 이미지를 HSV로 변환
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            # ---② H,S 채널에 대한 히스토그램 계산
            hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
            # ---③ 0~1로 정규화
            cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
            hists.append(hist)

        query = hists[0]
        methods = {'CORREL': cv2.HISTCMP_CORREL, 'CHISQR': cv2.HISTCMP_CHISQR,
                   'INTERSECT': cv2.HISTCMP_INTERSECT,
                   'BHATTACHARYYA': cv2.HISTCMP_BHATTACHARYYA}
        for j, (name, flag) in enumerate(methods.items()):
            print('%-10s' % name, end='\t')
            for k, (hist, img) in enumerate(zip(hists, imgs)):
                # ---④ 각 메서드에 따라 img1과 각 이미지의 히스토그램 비교
                ret = cv2.compareHist(query, hist, flag)
                if flag == cv2.HISTCMP_INTERSECT:  # 교차 분석인 경우
                    ret = ret / np.sum(query)  # 비교대상으로 나누어 1로 정규화
                print("img%d:%7.2f" % (k + 1, ret), end='\t')
            print()






    cv2.imshow('result', img_frame)
    # 27 == ESC
    key = cv2.waitKey(1)
    if key == 27:
        break
