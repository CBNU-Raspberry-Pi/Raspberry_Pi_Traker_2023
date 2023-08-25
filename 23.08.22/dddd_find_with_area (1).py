import cv2
import numpy as np
import tkinter as tk 
from adafruit_servokit import ServoKit



global th1,th2,th3,start

ini_loc = np.array([320,240])

th1 = 50
th2 = 50
th3 = 50
start = -1

hr = 10
sr = 10
vr = 10

def start_m():
    global start
    start *= -1
    


root = tk.Tk()
root.title("Set H,S,V area")
button1 = tk.Scale(root, from_=0, to=179, orient="horizontal", command=hr,length=250)
button1.pack()
button2 = tk.Scale(root, from_=0, to=255, orient="horizontal", command=sr,length=250)
button2.pack()
button3 = tk.Scale(root, from_=0, to=255, orient="horizontal", command=vr,length=250)
button3.pack()
button4 = tk.Button(root, text="start", command=start_m)
button4.pack()

pca = ServoKit(channels=16)

pca.servo[1].angle = 90
pca.servo[0].angle = 90

y_rad = 90
x_rad = 90


## 초기 물체의 색상 및 위치 정하기 

def click_event(event, x, y,w,t):
    global th1,th2,th3,ini_loc
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv_value = hsv_image[y, x]
        ini_loc = np.array([int(x), int(y)])
        print(f"HSV Value at clicked position ({x}, {y}):{hsv_value}")
        th1= hsv_value[0]
        th2= hsv_value[1]
        th3= hsv_value[2]




def hsv_bin(image, h_range, s_range, v_range):

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


    lower_bound = np.array([h_range[0], s_range[0], v_range[0]])
    upper_bound = np.array([h_range[1], s_range[1], v_range[1]])


    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)


    return mask


def hsvimg(hue, saturation, value):

    bgr_color = np.array(cv2.cvtColor(np.uint8([[[hue, saturation, value]]]), cv2.COLOR_HSV2BGR)[0][0], dtype=np.uint8)

    color_image = np.full((150, 150, 3), bgr_color)

    return color_image


cap = cv2.VideoCapture(0,cv2.CAP_V4L2)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
cap.set(cv2.CAP_PROP_FPS, 20)

# h_range = [10,30]
# s_range = [0,150]
# v_range = [255,255]


cv2.namedWindow("dd")  
cv2.setMouseCallback("dd", click_event) 



while 1:

    root.update()

    hr = int(button1.get())
    sr = int(button2.get())
    vr = int(button3.get())

    img = hsvimg(th1,th2,th3)

    cv2.imshow("hcv",img)

    ret,frame = cap.read()

    cv2.imshow("dd",frame)

    h_range = [th1-int(hr),th1+int(hr)]
    if h_range[0] <= 0:
        h_range[0] = 0
    if h_range[1] >= 179:
        h_range[1] = 179
    s_range = [th2-int(sr),th2+int(sr)]
    if s_range[0] <= 0:
       s_range[0] = 0
    if s_range[1] >= 255:
        s_range[1] = 255
    v_range = [th3-int(vr),th3+int(vr)]
    if v_range[0] <= 0:
        v_range[0] = 0
    if v_range[1] >= 255:
        v_range[1] = 255


    frame2 = hsv_bin(frame,h_range,s_range,v_range)


    ## 이상하게 라즈베리파이에선 이거 쓰면 느려서 아래로 대체 
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, ( 5, 5 ) ) ## 커널의 크기 설정 
    # img_mask = cv2.morphologyEx(frame2, cv2.MORPH_DILATE, kernel, iterations = 1) ## 모폴로지 확대 연산 

    
    ## 위와 동일한 역할을 하는 코드 
    kernel = np.ones((5, 5)) ## 이미지 커널 설정 
    img_mask = cv2.dilate(frame2, kernel, 1) ## 이미지 dilate화

    cv2.imshow("mo",img_mask)


    # nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(img_mask) ## 모폴로지한 연산의 영역값들 
    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(frame2) ## 모폴로지한 연산의 영역값들 

    max = -1 
    max_index = -1 

    for i in range(nlabels): ## 각 영역에서 
  
        if i < 1: ## 0인덱스는 넘어감  
            continue

        area = stats[i, cv2.CC_STAT_AREA] ## 영역의 크기 

        if area > max: ## 만약 두 점 사이의 거리가 최소값인경우 
            max = area ## 
            max_index = i ## 영역의 크기 인덱스를 설정 


    if max_index != -1: ## 최소 인덱스값을 찾았을 경우 


        center_x = int(centroids[max_index, 0])
        center_y = int(centroids[max_index, 1]) 
        left = stats[max_index, cv2.CC_STAT_LEFT]
        top = stats[max_index, cv2.CC_STAT_TOP]
        width = stats[max_index, cv2.CC_STAT_WIDTH]
        height = stats[max_index, cv2.CC_STAT_HEIGHT]


        cv2.rectangle(frame, (left, top), (left + width, top + height), (0, 0, 255), 5) ## img)color에 표시 
        cv2.circle(frame, (center_x, center_y), 10, (0, 255, 0), -1)
        
        
        ini_loc = np.array([center_x,center_y])
        
    
    if  start == 1 and np.linalg.norm(ini_loc- np.array((160,120))) > 14: ## 14가 중앙에서 위치까지의 거리 이 숫자를 통해 추적할 범위 조절 가능  
        

        y = ini_loc[1]
        
        y_loc = y - 120
        
        y_rot = int(y_loc/15)
        
        print(y_rot)
        
        y_rad -= y_rot
        
        ini_loc[1] = 120
        
        print(y_rad)
        
        if y_rad < 10:
            y_rad = 10
        elif y_rad > 170:
            y_rad = 170
            
        
        x = ini_loc[0]
        
        x_loc = x - 160
        
        x_rot = int(x_loc/15)
        
        print(x_rot)
        
        x_rad += x_rot
        
        ini_loc[0] = 160
        
        print(x_rad)
        
        if x_rad < 10:
            x_rad = 10
        elif x_rad > 170:
            x_rad = 170
            
        
        
        pca.servo[1].angle = x_rad
        pca.servo[0].angle = y_rad
 
        

    cv2.imshow("compl",frame)
    # print(ini_loc)
    

    cv2.waitKey(1)