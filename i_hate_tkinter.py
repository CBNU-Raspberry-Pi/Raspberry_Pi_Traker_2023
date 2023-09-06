import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from adafruit_servokit import ServoKit
import matplotlib.pyplot as plt
import time

pca = ServoKit(channels=16)

pca.servo[1].angle = 90
pca.servo[0].angle = 90

y_rad = 90
x_rad = 90

y_st = 1
x_st = 1


times =  []
x_rads = []
y_rads = []

start = -1

ini_loc = np.array([320,240])

th1 = 50
th2 = 50
th3 = 50
start = -1

hr = 10
sr = 10
vr = 10

cur_hsl = [th1,th2,th3,hr,sr,vr]
pre_hsl = [th1,th2,th3,hr,sr,vr-1]


root = tk.Tk()
root.geometry("650x490")


def hsvimg2(hue, light, saturation,h_range,l_range,s_range):


    bgr_color = np.array(cv2.cvtColor(np.uint8([[[hue, light, saturation]]]), cv2.COLOR_HLS2RGB)[0][0], dtype=np.uint8)


    color_image = np.full((240, 320, 3), bgr_color)

    h_length = h_range[1] - h_range[0]
    l_length = l_range[1] - l_range[0]
    s_length = s_range[1] - s_range[0]

    h_image = np.full((60, h_length, 3), bgr_color)
    l_image = np.full((60, l_length, 3), bgr_color)
    s_image = np.full((60, s_length, 3), bgr_color)




    for i in range(h_length):

        h_color = np.array(cv2.cvtColor(np.uint8([[[h_range[0]+i, light, saturation]]]), cv2.COLOR_HLS2RGB)[0][0], dtype=np.uint8)
        cv2.line(h_image, (i , 1), (i, 60), (int(h_color[0]),int(h_color[1]),int(h_color[2])), 1, cv2.LINE_4)


    h_image = cv2.resize(h_image,(320,60))

    for i in range(l_length):

        l_color = np.array(cv2.cvtColor(np.uint8([[[hue, l_range[0]+i, saturation]]]), cv2.COLOR_HLS2RGB)[0][0], dtype=np.uint8)
        cv2.line(l_image, (i , 1), (i, 60), (int(l_color[0]),int(l_color[1]),int(l_color[2])), 1, cv2.LINE_4)

    l_image = cv2.resize(l_image,(320,60))

    for i in range(s_length):

        s_color = np.array(cv2.cvtColor(np.uint8([[[hue, light, s_range[0]+i]]]), cv2.COLOR_HLS2RGB)[0][0], dtype=np.uint8)
        cv2.line(s_image, (i , 1), (i, 60), (int(s_color[0]),int(s_color[1]),int(s_color[2])), 1, cv2.LINE_4)

    s_image = cv2.resize(s_image,(320,60))


    color_image[60:120,0:320] = h_image
    color_image[120:180,0:320] = l_image
    color_image[180:240,0:320] = s_image


    return color_image


def retxt(name):
    clist = []
    rf = open("{0}.txt".format(name), "r", encoding="utf8")
    for i in rf:
        i = float(i)
        clist.append(i)
    rf.close()
    return clist

list4 = retxt("shit")


def start_m():
    global start
    start *= -1
    
def quit_m():
    global start
    start = 2

def hsv_bin(image, h_range, l_range, s_range):

    hls_image = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)


    lower_bound = np.array([h_range[0], l_range[0], s_range[0]])
    upper_bound = np.array([h_range[1], l_range[1], s_range[1]])


    mask = cv2.inRange(hls_image, lower_bound, upper_bound)


    return mask

def hsvimg(hue, light, saturation):

    bgr_color = np.array(cv2.cvtColor(np.uint8([[[hue, light, saturation]]]), cv2.COLOR_HLS2RGB)[0][0], dtype=np.uint8)

    color_image = np.full((240, 320, 3), bgr_color)

    return color_image

def on_canvas_click(event):
    global click_x,click_y,frame,th1,th2,th3,ini_loc
    x = event.x
    y = event.y
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_RGB2HLS)
    hsv_value = hsv_image[y, x]
    ini_loc = np.array([int(x), int(y)])
    print(f"HSV Value at clicked position ({x}, {y}):{hsv_value}")
    th1= hsv_value[0]
    th2= hsv_value[1]
    th3= hsv_value[2]

## Set Canvas img location 
canvas1 = tk.Canvas(root, width=320, height=240)
canvas1.grid(row=0,column=0)

canvas1.bind("<Button-1>", on_canvas_click)

## Set mono img location 

mono = tk.Label(root)
mono.grid(row=1,column=0)

## Set location img location 

draw_circle = tk.Label(root)
draw_circle.grid(row=0,column=1)

## Set color location

set_color = tk.Label(root)
set_color.grid(row=1,column=1)


##조정 버튼


root2 = tk.Tk()
root2.title("Set H,S,V area")
button1 = tk.Scale(root2, from_=1, to=91, orient="horizontal", length=250)
button1.pack()
button2 = tk.Scale(root2, from_=1, to=255, orient="horizontal", length=250)
button2.pack()
button3 = tk.Scale(root2, from_=1, to=255, orient="horizontal", length=250)
button3.pack()
button4 = tk.Scale(root2, from_=0, to=3, orient="horizontal", length=250,resolution = 0.01)
button4.pack()
button5 = tk.Button(root2, text="start", command=start_m)
button5.pack()
button6 = tk.Button(root2, text="quit", command=quit_m)
button6.pack()
button7 = tk.Scale(root2, from_=1, to=240, orient="horizontal", length=250)
button7.pack()
button8 = tk.Scale(root2, from_=1, to=320, orient="horizontal", length=250)
button8.pack()


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
cap.set(cv2.CAP_PROP_FPS, 30)


def set_update():
    global frame,start,x_rads,y_rads,times,sta,ini_loc,x_rad,y_rad,pca,x_st,y_st,cur_hsl,pre_hsl,th1,th2,th3,colorimg,pre_xrad,pre_yrad,move
    ret,frame = cap.read()

    

    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame2 = frame.copy()
    
    cv2.line(frame,(1,y_st),(320,y_st),(0,0,0),1,cv2.LINE_AA)
    cv2.line(frame,(x_st,1),(x_st,240),(0,0,0),1,cv2.LINE_AA)
    
    

    hr = int(button1.get())
    sr = int(button2.get())
    vr = int(button3.get())
    distance = button4.get()
    y_st = int(button7.get())
    x_st = int(button8.get())

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
    
    cur_hsl = [th1,th2,th3,hr,sr,vr]

    monoimg = hsv_bin(frame,h_range,s_range,v_range)
    kernel = np.ones((5, 5)) ## 이미지 커널 설정 
    monoimg = cv2.dilate(monoimg, kernel, 3) ## 이미지 dilate화

    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(monoimg) ## 모폴로지한 연산의 영역값들 

    max = -1 
    max_index = -1 

    for i in range(nlabels): ## 각 영역에서 
  
        if i < 1: ## 0인덱스는 넘어감  
            continue

        area = stats[i, cv2.CC_STAT_AREA] ## 영역의 크기 

        if area > max and area > 10:  
            max = area ## 
            max_index = i 


    if max_index != -1: ## 


        center_x = int(centroids[max_index, 0])
        center_y = int(centroids[max_index, 1]) 
        left = stats[max_index, cv2.CC_STAT_LEFT]
        top = stats[max_index, cv2.CC_STAT_TOP]
        width = stats[max_index, cv2.CC_STAT_WIDTH]
        height = stats[max_index, cv2.CC_STAT_HEIGHT]


        cv2.rectangle(frame, (left, top), (left + width, top + height), (0, 0, 255), 5) ## img)color에 표시 
        cv2.circle(frame, (center_x, center_y), 3, (0, 255, 0), -1)
        
        
        ini_loc = np.array([center_x,center_y])


    root2.update()


    
    if  start == 1:
        
    
        
        current = time.time() - sta
        times.append(current)
        
#         x_dist = round((distance*np.cos(np.radians(abs(y_rad-90)))*list4[x_rad-10]),5)
#         y_dist = round((distance*np.cos(np.radians(abs(x_rad-90)))*list4[y_rad-10]),5)
#         
#         print(x_dist,"x")
#         print(y_dist,"y")
        
        x_rads.append(x_rad)
        y_rads.append(y_rad)
    
        if np.linalg.norm(ini_loc- np.array((160,120))) > 15:
        

            y = ini_loc[1]      
            y_loc = y - 120   
            y_rot = int(y_loc/20) 
            
            y_rad -= y_rot
            
            ini_loc[1] = 120
#             
#             print(y_rad)
            
            if y_rad < 10:
                y_rad = 10
            elif y_rad > 170:
                y_rad = 170
                
            
            x = ini_loc[0]
            x_loc = x - 160       
            x_rot = int(x_loc/20)
            
            x_rad += x_rot
            
            ini_loc[0] = 160
#             
            
            
            if x_rad < 10:
                x_rad = 10
            elif x_rad > 170:
                x_rad = 170
                
#             print(x_rad)
        cv2.line(move,(pre_xrad,180-pre_yrad),(x_rad,180-y_rad),(255,255,255),1,cv2.LINE_4)
        pre_xrad = x_rad
        pre_yrad = y_rad 


            
            
            

            
    elif start == -1:
        
        sta = time.time()
        times = []
        x_rads = []
        y_rads = []
        
        move = np.zeros((180,180,3),dtype=np.uint8)
        
        pre_xrad = 90
        pre_yrad = 90
    
    elif start == 2:
        
#         x_dis = []
#         y_dis = []
# 
# 
#         for i in range(len(x_rads)):
#             
#             xd = round((distance*np.cos(np.radians(abs(y_rads[i]-90)))*list4[x_rads[i]-10]),5)
#             yd = round((distance*np.cos(np.radians(abs(x_rads[i]-90)))*list4[y_rads[i]-10]),5)
#             
#             x_dis.append(xd)
#             y_dis.append(yd)
            

        plt.plot(times,x_rads,label = "x axis")
        plt.plot(times,y_rads,label = "y axis")

        plt.legend()
        plt.ylabel("x, y axis (pixel)")
        plt.xlabel("time(second)")

        plt.show()
        
        x_rad = 90
        y_rad = 90
        
        start = -1
    
    pca.servo[1].angle = x_rad
    pca.servo[0].angle = y_rad
    
    canvas_img= Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image = canvas_img)
    canvas1.imgtk = imgtk

    canvas1.create_image(0, 0, image=imgtk, anchor=tk.NW)

    
    set_mono_img= Image.fromarray(monoimg)
    imgtk1 = ImageTk.PhotoImage(image = set_mono_img)
    mono.imgtk = imgtk1
    mono.configure(image=imgtk1)
    
    move1 = cv2.resize(move,(320,240))
    
    draw_circle_img= Image.fromarray(move1)
    imgtk2 = ImageTk.PhotoImage(image = draw_circle_img)
    draw_circle.imgtk = imgtk2
    draw_circle.configure(image=imgtk2)
    
    if cur_hsl != pre_hsl:
        colorimg = hsvimg2(th1,th2,th3,h_range,s_range,v_range)
    
    pre_hsl[:] = cur_hsl[:]

    set_color_img= Image.fromarray(colorimg)
    imgtk3 = ImageTk.PhotoImage(image = set_color_img)
    set_color.imgtk = imgtk3
    set_color.configure(image=imgtk3)
        
        


    root.after(1,set_update)



set_update()

root.mainloop()


