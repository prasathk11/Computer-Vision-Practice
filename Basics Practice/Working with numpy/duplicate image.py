import cv2 as cv
import numpy as np

img=cv.imread("ball.jpg")

img=cv.rectangle(img,(88,250),(277,72),(255,0,0),2)
img=cv.rectangle(img,(530,333),(693,144),(255,0,0),2)

myimg= img[250:72 , 88:280]
img[316:144 , 520:712]=myimg
cv.imshow("Image",img)
cv.waitKey(0)
cv.destroyAllWindows()


#def event_click(event,x,y,flag,param):
#    if event==cv.EVENT_LBUTTONDOWN:
#        font=cv.FONT_HERSHEY_SIMPLEX
#        strXY=str(x)+","+str(y)
#        cv.putText(img,strXY,(x,y),font,1,(255,0,0),2)
#        cv.imshow("Image",img)
