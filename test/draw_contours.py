import cv2
import numpy as np
import contours as ct





def draw_contours(total_sketch,contours,thr): ## contours그리기 total_sketch와 contours를 받아오면 total_sketch에서 해당하는 점의 좌표값을 얻음

    for contour in contours:

        cv2.drawContours(image=total_sketch, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

        # 사각형과 점 표시
        
        if cv2.contourArea(contour) < thr: ##만약 경계의 크기가 thr이하일경우 넘어감 

            continue
        # print(cv2.contourArea(contour))
        (x, y, w, h) = cv2.boundingRect(contour)

        # print(ini_loc,"hmm")

        cv2.circle(img=total_sketch, center=(int((2*x+w)/2),int((2*y+h)/2)),radius=int((thr/3)**0.5), color=(0, 0, 255), thickness=2)
        cv2.rectangle(img=total_sketch, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
        # print(int((2*x+w)/2),int((2*y+h)/2))
        # ini_loc = [int((2*x+w)/2),int((2*y+h)/2)]
    print()

    return total_sketch





