import numpy as np
import cv2 as cv


def event_click(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x,",",y)
        font = cv.FONT_HERSHEY_SIMPLEX
        strXY = str(x)+","+str(y)
        cv.putText(img,strXY,(x,y),font,1,(15,0,233),2)
        cv.imshow("Image", img)


img =cv.imread("ball.jpg")

cv.imshow("Image",img)
cv.setMouseCallback("Image",event_click)
cv.waitKey(0)
cv.destroyAllWindows()