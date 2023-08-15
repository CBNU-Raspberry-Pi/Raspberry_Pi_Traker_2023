import cv2
import contours as ct
import numpy as np
import tkinter as tk
import img_div as dv
import matplotlib.pyplot as plt
import find_one as fo
import time 
from adafruit_servokit import ServoKit
import cacul_rot as cr 



pca = ServoKit(channels=16)

# 변수 초기화


global hmm,th1,t,st,th2

hmm = (2,2)

start = time.time()
th1 = 50
th2 = 50

t = 2
st = -1

old_loc = np.array((320,240)) 
ini_loc = np.array((320,240))

# if not cam.isOpened():
#     print("Could not open webcam")
#     exit()

xloc_data = []
yloc_data = []
time_data = []

move = np.zeros((480,640,3),dtype=np.uint8)

y_rad = 90
x_rad = 90

def change_text():
    global th1
    th1 = button.get()

def change_text2():
    global th2
    th2 = button2.get()

def change_text3():
    global t
    t -= 2

def change_text4():
    global st
    st*= -1

# 숫자 변경 함수

# UI 구성
root = tk.Tk()
root.title("gray thresh")
button = tk.Scale(root, from_=0, to=200, orient="horizontal", command=th1,length=250)
button.pack()
button11 = tk.Button(root, text="Change", command=change_text)
button11.pack()


root2 = tk.Tk()
root2.title("size thresh")
button2 = tk.Scale(root2, from_=1, to=2500, orient="horizontal", command=th2,length=250)
button2.pack()
button22 = tk.Button(root2, text="Change", command=change_text2)
button22.pack()

root3 = tk.Tk()
root3.title("quit")
button33 = tk.Button(root3, text="quit", command=change_text3)
button33.pack()

root4 = tk.Tk()
root4.title("Button")
button33 = tk.Button(root4, text="Button", command=change_text4)
button33.pack()



pca.servo[1].angle = 90
pca.servo[0].angle = 90


cam = cv2.VideoCapture(0) ## 카메라 끌떄 오류 안나오도록
cam.set(cv2.CAP_PROP_POS_FRAMES,30)
status, frame = cam.read()

h,w,c = frame.shape


if not cam.isOpened():
    print("Could not open webcam")
    exit()

while cam.isOpened():
    status, frame = cam.read()
    
    
    root.update()
#     root2.update()
    root3.update()
    root4.update()

    
    if t == -1:
        break
    
    

    # cv2.imshow("current", frame)
#     frame = cv2.flip(frame,1)
#     frame = cv2.flip(frame,0)
    frame2 = frame[:,:,2]
    cv2.imshow("red",frame2)
#     frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) ## 새로받은 이미지 흑백처리
    frame2 = cv2.GaussianBlur(src=frame2, ksize=(5, 5), sigmaX=0)
    
    
    
    if np.linalg.norm(ini_loc- np.array((320,240))) > 25:
        

        y = ini_loc[1]
        
        y_loc = y - 240
        
        y_rot = int(y_loc/25)
        
        print(y_rot)
        
        y_rad -= y_rot
        
        ini_loc[1] = 240
        
        print(y_rad)
        
        if y_rad < 10:
            y_rad = 10
        elif y_rad > 170:
            y_rad = 170
            
        
        x = ini_loc[0]
        
        x_loc = x - 320
        
        x_rot = int(x_loc/25)
        
        print(x_rot)
        
        x_rad += x_rot
        
        ini_loc[0] = 320
        
        print(x_rad)
        
        if x_rad < 10:
            x_rad = 10
        elif x_rad > 170:
            x_rad = 170
            
        
        
        pca.servo[1].angle = x_rad
        pca.servo[0].angle = y_rad
        
        pre_frame = frame2
        
        t += 0
        
    
    

        
        
        
        
    

    if t == 1:

#         h,w = frame2.shape
        total_sketch = np.zeros((h,w,3),dtype=np.uint8)
        total_sketch[:,:] = frame[:,:]

        # cv2.imshow("pre",pre_frame)
        # cv2.imshow("current2", frame2)

        ctr = ct.find_contours(pre_frame,frame2,th1)
#         print(fo.draw_contours(ini_loc,ctr,th2))
 
        ini_loc = fo.draw_contours(ini_loc,ctr,th2)[0]
#         th2 = fo.draw_contours(ini_loc,ctr,th2)[1]
        
        
        # cv2.imshow("con",img)
        


        cv2.putText(total_sketch, str(th1), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(total_sketch, str(th2), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


#         hmm = dv.img_div(total_sketch,ini_loc)
        cv2.circle(img=total_sketch, center=(ini_loc[0],ini_loc[1]),radius=int((th2/3)**0.5), color=(0, 0, 255), thickness=2)
        cv2.line(move,old_loc,ini_loc,(0,120,120),1,cv2.LINE_4)

        
#         cv2.imshow("current2", move)


        old_loc = ini_loc
    
        if st == 1:

            time_data.append(time.time()-start)
            xloc_data.append(ini_loc[0])
            yloc_data.append(ini_loc[1])


            cv2.line(move,old_loc,ini_loc,(0,0,255),1,cv2.LINE_4)
            cv2.imshow("loc", move)
            
        elif st == -1:

            xloc_data = []
            yloc_data = []
            time_data = []


            move = np.zeros((480,640,3),dtype=np.uint8)
            cv2.putText(total_sketch, str("STOP"), (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("loc", move)
            start = time.time()
        
#         total_sketch = cv2.rotate(total_sketch,cv2.ROTATE_90_CLOCKWISE)
        
        cv2.imshow("current3", total_sketch)
    
    cv2.waitKey(1)
    
   

    pre_frame = frame2
    if t>=2:
        
        pre_frame = frame2
        cv2.imshow("current3", frame)
        
        t -= 1 

cam.release()
cv2.destroyAllWindows()

plt.plot(time_data,xloc_data,label = "x axis")
plt.plot(time_data,yloc_data,label = "y axis")

plt.legend()
plt.ylabel("x, y axis (pixel)")
plt.xlabel("time(second)")

plt.show()


