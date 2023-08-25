import cv2
import numpy as np
import contours as ct




def draw_contours(ini_loc,contours,thr): ## contours중에서 기준이 되는 점과 가장 가까운 contour좌표 를 찾아내서 반환 

    short = 10000
    short_loc = ini_loc
    
    for contour in contours:

        # cv2.drawContours(image=total_sketch, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

        # 사각형과 점 표시
        
        if cv2.contourArea(contour) < thr: ##만약 경계의 크기가 thr이하일경우 넘어감 

            continue
        # print(cv2.contourArea(contour))
        (x, y, w, h) = cv2.boundingRect(contour)

        # print(ini_loc,"hmm")
        x = int((2*x+w)/2)
        y = int((2*y+h)/2)

        temp = np.array((x,y))
        
        if np.linalg.norm(ini_loc-temp) < short:
            short = np.linalg.norm(ini_loc-temp)
            short_loc = np.array((x,y))

        
    ini_loc = short_loc
    return ini_loc







