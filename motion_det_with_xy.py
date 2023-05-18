import cv2
import numpy as np
from PIL import ImageGrab

def motion_detector_gist():
  t = 0
  # cap = cv2.VideoCapture('output.mp4')
  cap = cv2.VideoCapture(0)
  ret, frame = cap.read()
  print(frame.shape)

  previous_frame = None
  ini_loc = [int(frame.shape[0]/2),int(frame.shape[0]/2)]
  
  while (cap.isOpened()==1):
    print("start")
    ret, frame = cap.read()

        # 1. Load image; convert to RGB
    img_rgb = frame

    # img_rgb = cv2.cvtColor(src=img_brg, code=cv2.COLOR_BGR2RGB)


    # 2. Prepare image; grayscale and blur
    prepared_frame = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    prepared_frame = cv2.GaussianBlur(src=prepared_frame, ksize=(5, 5), sigmaX=0)

    # 2. Calculate the difference
    if (previous_frame is None):
      # First frame; there is no previous one yet
      previous_frame = prepared_frame
      continue

    # 3. calculate difference and update previous frame
    diff_frame = cv2.absdiff(src1=previous_frame, src2=prepared_frame)
    previous_frame = prepared_frame

    # 4. Dilute the image a bit to make differences more seeable; more suitable for contour detection
    kernel = np.ones((15, 15))
    diff_frame = cv2.dilate(diff_frame, kernel, 1)

    # 5. Only take different areas that are different enough (>20 / 255)
    thresh_frame = cv2.threshold(src=diff_frame, thresh=100, maxval=255, type=cv2.THRESH_BINARY)[1]

    # 6. Find and optionally draw contours
    contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
      if cv2.contourArea(contour) < 50:
          continue
      (x, y, w, h) = cv2.boundingRect(contour)

      print(ini_loc,"hmm")
     
      cv2.circle(img=img_rgb, center=(int((2*x+w)/2),int((2*y+h)/2)),radius=10, color=(0, 0, 255), thickness=2)
      cv2.rectangle(img=img_rgb, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
      ini_loc = [int((2*x+w)/2),int((2*y+h)/2)]


    cv2.imshow('Motion detector', img_rgb)

    print("shit")
    if (cv2.waitKey(30) == 27):
      # out.release()
      break

  # Cleanup
  cv2.destroyAllWindows()

if __name__ == "__main__":
  motion_detector_gist()