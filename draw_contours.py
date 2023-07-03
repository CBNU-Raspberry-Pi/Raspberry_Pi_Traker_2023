import cv2
import numpy as np
import contours as ct




    
def draw_contours(total_sketch,contours,thr): ## contours그리기 total_sketch와 contours를 받아오면 total_sketch에서 해당하는 점의 좌표값을 얻음

    for contour in contours:

        # cv2.drawContours(image=total_sketch, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

        # 사각형과 점 표시
        
        if cv2.contourArea(contour) < thr: ##만약 경계의 크기가 thr이하일경우 넘어감 

            continue
        print(cv2.contourArea(contour))
        (x, y, w, h) = cv2.boundingRect(contour)

        # print(ini_loc,"hmm")

        cv2.circle(img=total_sketch, center=(int((2*x+w)/2),int((2*y+h)/2)),radius=int((thr/3)**0.5), color=(0, 0, 255), thickness=2)
        cv2.rectangle(img=total_sketch, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
        # ini_loc = [int((2*x+w)/2),int((2*y+h)/2)]
    print()

    return total_sketch

## test코드  모듈로 사용할때는 아래부분 주석처리할것 

# img1 = cv2.imread('img.jpg')

# h,w,c = img1.shape

# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) ## 새로받은 이미지 흑백처리
# img1 = cv2.GaussianBlur(src=img1, ksize=(5, 5), sigmaX=0)

# img2 = cv2.imread('img1.jpg')
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) ## 새로받은 이미지 흑백처리
# img2 = cv2.GaussianBlur(src=img2, ksize=(5, 5), sigmaX=0)

# print(h,w)

# total_sketch = np.zeros((h,w,3),dtype=np.uint8)

# contours = ct.find_contours(img1,img2,105)


# total = draw_contours(total_sketch,contours)

# cv2.imshow('Motion detect', img1)
# cv2.imshow('Motion detecr', img2)
# cv2.imshow('Motion detector', total) ## contours와 점 표시 
# cv2.waitKey(0)









