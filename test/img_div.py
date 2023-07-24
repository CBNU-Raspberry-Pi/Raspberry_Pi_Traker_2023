import cv2
import numpy as np 

# 카메라 640x480해상도를 기준으로 제작

height = 96
width  = 128



def img_div(img,ini_loc):
    short = 1000
    short_loc = ((129,97),(256,192))

    for i in range(5):
        for j in range(5):
            pt1 = ((1+width*i),(1+height*j))
            pt2 = ((width*(i+1)),(height*(j+1)))

            center = np.array((int((pt1[0]+pt2[0])/2)+1,int((pt1[1]+pt2[1])/2)+1))

            if np.linalg.norm(ini_loc-center) < short:
                short = np.linalg.norm(ini_loc-center)
                short_loc = (pt1,pt2)
                retu_loc = (i,j)

            cv2.rectangle(img,pt1,pt2,(255,255,255),1)
    
    cv2.rectangle(img,short_loc[0],short_loc[1],(255,255,255),-1)

    return retu_loc

