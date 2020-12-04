import cv2 as cv
import numpy as np


def display(x):
    print(x)


cv.namedWindow("BGR TrackBar")

cv.createTrackbar("Image","BGR TrackBar",0,255,display)


switch="Color/Gray"
cv.createTrackbar(switch,"BGR TrackBar",0,1,display)


while(1):
    img = cv.imread("ball.jpg")
    pos = cv.getTrackbarPos("Image","BGR TrackBar")
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img,str(pos),(400,100),font,2,(0,0,255),4)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    S = cv.getTrackbarPos(switch,"BGR TrackBar")
    if S==0:
        pass
    else:
        img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

    cv.imshow("BGR TrackBar",img)


cv.destroyAllWindows()
