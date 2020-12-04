import numpy as np
import cv2 as cv

def circle(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y), 50, (35,100,178), -1)

cv.namedWindow(winname="my_drawing")

cv.setMouseCallback("my_drawing",circle)
img=np.zeros([512,512,3],np.int8)
while True:
    cv.imshow("my_drawing",img)
    if cv.waitKey(5) & 0xFF == ord('e'):
        break

cv.destroyAllWindows()