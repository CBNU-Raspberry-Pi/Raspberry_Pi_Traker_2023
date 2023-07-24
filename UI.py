import cv2
import contours as ct
import draw_contours as dr
import numpy as np
import tkinter as tk
import find_one as fo
import img_div as dv

# 변수 초기화

th1 = 50
th2 = 50


def change_text():
    global th1
    th1 = button.get()

def change_text2():
    global th2
    th2 = button2.get()


# 숫자 변경 함수


# UI 구성
window = tk.Tk()
window.title("gray thresh")
button = tk.Scale(window, from_=0, to=200, orient="horizontal", command=th1,length=250)
button.pack()
button11 = tk.Button(window, text="Change", command=change_text)
button11.pack()

button2 = tk.Scale(window, from_=1, to=2500, orient="horizontal", command=th2,length=250)
button2.pack()
button22 = tk.Button(window, text="Change", command=change_text2)
button22.pack()



pre_frame = 0

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW) ## 카메라 끌떄 오류 안나오도록 
cam.set(cv2.CAP_PROP_FPS,60)


t = 0 
ini_loc = np.array((320,240))

if not cam.isOpened():
    print("Could not open webcam")
    exit()

while cam.isOpened():
    status, frame = cam.read()

    # cv2.imshow("current", frame)
    frame = cv2.flip(frame,1)

    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) ## 새로받은 이미지 흑백처리
    frame2 = cv2.GaussianBlur(src=frame2, ksize=(5, 5), sigmaX=0)

    if t != 0:

        h,w = frame2.shape
        total_sketch = np.zeros((h,w,3),dtype=np.uint8)
        total_sketch[:,:] = frame[:,:]

        # cv2.imshow("pre",pre_frame)
        # cv2.imshow("current2", frame2)
        ctr = ct.find_contours(pre_frame,frame2,th1)
        ini_loc = fo.draw_contours(ini_loc,ctr,th2)

        
        # cv2.imshow("con",img)
        


        cv2.putText(total_sketch, str(th1), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(total_sketch, str(th2), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        window.update()

        hmm = dv.img_div(total_sketch,ini_loc)
        cv2.circle(img=total_sketch, center=(ini_loc[0],ini_loc[1]),radius=int((th2/3)**0.5), color=(0, 0, 255), thickness=2)
        cv2.imshow("current3", total_sketch)
        

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    pre_frame = frame2
    t = 1 

cam.release()
cv2.destroyAllWindows()