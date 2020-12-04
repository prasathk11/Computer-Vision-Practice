import cv2 as cv
import numpy as np

def event_click(event,x,y,flag,param):
    if event==cv.EVENT_LBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv.FONT_HERSHEY_SIMPLEX
        strXY=str(blue)+","+str(green)+","+str(red)
        cv.putText(img,strXY,(x,y),font,2,(21,33,234),2)
        cv.imshow("Image",img)


img= cv.imread("csk.jpg")
cv.imshow("Image",img)

cv.setMouseCallback("Image",event_click)

cv.waitKey(0)
cv.destroyAllWindows()