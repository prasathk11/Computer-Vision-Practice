import cv2 as cv
import numpy as np

# Function
# x,y, flags, param are feed from OpenCV automaticaly
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,
                  (x, y),
                  100,
                  (75, 131, 252),
                  -1)
    elif event == cv.ENVENT_RBUTTONDOWN:
        cv.circle(img,
                  (x, y),
                  50,
                  (251, 75, 131),
                  -1)

    # Left Button Down

    # Right Button Down


# Connect the Function with the Callback
cv.namedWindow(winname="my_draw")

# Callback
cv.setMouseCallback("my_draw", draw_circle)

# Using OpenCV to show the Image
img = np.zeros([512, 512, 3], np.int8)

while True:
    cv.imshow("my_draw", img)
    if cv.waitKey(5) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()

