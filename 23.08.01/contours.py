import cv2
import numpy as np

# 흑백 이미지와 임계값을 받아서 가우시안 처리 크기와 임계값을 설정 

# img 1은 흑백처리된 상태이어야함 img1은 이전이미지 img2는 새로 받은 이미지 

def find_contours(img1,img2,thr):

    # img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) ## 새로받은 이미지 흑백처리
    # img2 = cv2.GaussianBlur(src=img2, ksize=(5, 5), sigmaX=0)

    diff_frame = cv2.absdiff(src1=img1, src2=img2)
    
    kernel = np.ones((15, 15)) ## 이미지 커널 설정 
    diff_frame = cv2.dilate(diff_frame, kernel, 1) ## 이미지 dilate화


    ## 이미지 임계값 설정 
    thresh_frame = cv2.threshold(src=diff_frame, thresh=thr, maxval=255, type=cv2.THRESH_BINARY)[1] ## 숫자가 작을수록 더 민감하게 반응 

    # 6. Find and optionally draw contours
    contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)


    return contours 

# img1 = cv2.imread('img.jpg')

# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) ## 새로받은 이미지 흑백처리
# img1 = cv2.GaussianBlur(src=img1, ksize=(5, 5), sigmaX=0)


# img2 = cv2.imread('img1.jpg')

# print(find_contours(img1,img2,100))



