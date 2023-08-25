import cv2
import contours as ct
import draw_contours as dr
import numpy as np
## 카메라는 메인함수에서만 구현해야함

pre_frame = 0

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW) ## 카메라 끌떄 오류 안나오도록 

t = 0 



if not cam.isOpened():
    print("Could not open webcam")
    exit()

while cam.isOpened():
    status, frame = cam.read()

    cv2.imshow("current", frame)

    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) ## 새로받은 이미지 흑백처리
    frame2 = cv2.GaussianBlur(src=frame2, ksize=(5, 5), sigmaX=0)

    if t != 0:

        h,w = frame2.shape
        # total_sketch = np.zeros((h,w,3),dtype=np.uint8)
        total_sketch = frame

        cv2.imshow("pre",pre_frame)
        cv2.imshow("current2", frame2)
        ctr = ct.find_contours(pre_frame,frame2,50)
        img = dr.draw_contours(total_sketch,ctr,50)
        # cv2.imshow("con",img)
        cv2.imshow("current3", total_sketch)
        


    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

    

    pre_frame = frame2
    t = 1 

cam.release()
cv2.destroyAllWindows()