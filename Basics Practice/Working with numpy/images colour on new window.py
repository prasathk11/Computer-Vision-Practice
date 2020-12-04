import cv2 as cv
import numpy as np


def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        Imagecolor = np.zeros((300, 300, 3), np.uint8)
        Imagecolor[:] = [blue, green, red]

        cv.imshow("BGR_COLOUR", Imagecolor)


img = cv.imread("csk.jpg")
cv.imshow("Image", img)

cv.setMouseCallback("Image", click_event)

cv.waitKey(0)
cv.destroyAllWindows()
