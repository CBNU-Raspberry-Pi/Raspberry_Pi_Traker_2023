## this code is from https://youtu.be/2IjZkPQT458
## this code is just tracking some specific colour
## in this code, some variables are named about "blue" but it track colour green
## I didn't recorrect variables names so do not confuse about it
## and also I recommend to know about HSV.


import cv2 as cv



def draw_ball_location(img_color, locations):
    for i in range(len(locations)-1):

        if locations[0] is None or locations[1] is None:
            continue

        cv.line(img_color, tuple(locations[i]), tuple(locations[i+1]), (0, 255, 255), 3)

    return img_color



cap = cv.VideoCapture(0)
# size(640, 480)
x_size = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
y_size = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))


list_ball_location = []
history_ball_locations = []
isDraw = True

while True:



    ret,img_color = cap.read()

    # drawing x, y axises
    cv.line(img_color, (0, y_size // 2), (x_size, y_size // 2), (0,0,0), 1)
    cv.line(img_color, (x_size // 2, 0), (x_size // 2, y_size), (0,0,0), 1)


    # reversing the video right and left
    img_color = cv.flip(img_color, 1)

    # changing colour map BGR to HSV
    img_hsv = cv.cvtColor(img_color, cv.COLOR_BGR2HSV)

    # changed, blue to green
    # red 0,green 60, blue 120
    hue_blue = 60
    # order : hue, satration, value
    lower_blue = (hue_blue-20, 200, 100)
    upper_blue = (hue_blue+20, 255, 255)
    img_mask = cv.inRange(img_hsv, lower_blue, upper_blue)

    kernel = cv.getStructuringElement( cv.MORPH_RECT, ( 5, 5 ) )
    img_mask = cv.morphologyEx(img_mask, cv.MORPH_DILATE, kernel, iterations = 3)




    nlabels, labels, stats, centroids = cv.connectedComponentsWithStats(img_mask)



    max = -1
    max_index = -1 

    for i in range(nlabels):
 
        if i < 1:
            continue

        area = stats[i, cv.CC_STAT_AREA]

        if area > max:
            max = area
            max_index = i


    if max_index != -1:


        center_x = int(centroids[max_index, 0])
        center_y = int(centroids[max_index, 1]) 
        left = stats[max_index, cv.CC_STAT_LEFT]
        top = stats[max_index, cv.CC_STAT_TOP]
        width = stats[max_index, cv.CC_STAT_WIDTH]
        height = stats[max_index, cv.CC_STAT_HEIGHT]


        cv.rectangle(img_color, (left, top), (left + width, top + height), (0, 0, 255), 5)
        cv.circle(img_color, (center_x, center_y), 10, (0, 255, 0), -1)

        if isDraw:
            list_ball_location.append((center_x, center_y))
            # printing the x, y axises (centre of video is (0, 0))
            print((center_x - (x_size // 2), (y_size // 2) - center_y))
            
        
        else:
            history_ball_locations.append(list_ball_location.copy())
            list_ball_location.clear()


    img_color = draw_ball_location(img_color, list_ball_location)

    for ball_locations in history_ball_locations:
        img_color = draw_ball_location(img_color, ball_locations)




    cv.imshow('Green', img_mask)
    cv.imshow('Result', img_color)

    # esc to quit, space bar to erase the yello orbit line, v to stop drawing
    key = cv.waitKey(1)
    if key == 27: # esc
        break
    elif key == 32: # space bar
        list_ball_location.clear()
        history_ball_locations.clear()
    elif key == ord('v'):
        isDraw = not isDraw
