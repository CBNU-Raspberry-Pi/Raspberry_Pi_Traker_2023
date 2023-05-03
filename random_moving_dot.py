import cv2
import numpy as np

## opencv2와 numpy 설치필요 

x = 375
y = 375

n = 10

t = 0

video = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (750,750))


while(t<250):
    total_sketch = np.zeros((750,750,3),dtype=np.uint8)
    next_position = np.random.randint(1,9)
    intv = np.random.randint(1,5)
    intv = 1
    
    he = {1:[-n,-n],
          2:[0,-n],
          3:[n,-n],
          4:[-n,-0],
          5:[n,0],
          6:[-n,n],
          7:[0,n],
          8:[n,n],
          }
    

    x += intv*he[next_position][0]
    y += intv*he[next_position][1]

    if x> 750-n:
        x -= intv*2*he[next_position][0]
    
    if y > 750-n:
        y -= intv*2*he[next_position][1]

    if x < n:
        x += intv*2*he[next_position][0]
    
    if y < n :
        y += intv*2*he[next_position][1]

        
    cv2.rectangle(total_sketch,(x-3,y-3),(x+3,y+3),(255,255,255),1,cv2.LINE_4)
    cv2.imshow("he",total_sketch)
    cv2.waitKey(50)

    video.write(total_sketch)

    t += 1

cv2.destroyAllWindows()
video.release()
            

