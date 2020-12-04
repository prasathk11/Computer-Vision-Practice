import cv2 as cv
import numpy as np

def click_event(event,x,y,flag,param):
    if event== cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),5,(0,255,0),-1)
        points.append((x,y))
        if len(points)>=2:
            cv.line(img,points[-1],points[-2],(0,255,255),2)
        cv.imshow("Image",img)

img=np.zeros([512,512,3],np.uint8)
cv.imshow("Image",img)

points=[]
cv.setMouseCallback("Image",click_event)
cv.waitKey(0)
cv.destroyAllWindows()
