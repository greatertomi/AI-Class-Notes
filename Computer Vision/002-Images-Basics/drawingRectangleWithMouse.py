import cv2
import numpy as np

# VARIABLES
drawing = False
ix, iy = -1, -1


# FUNCTION
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)


# SHOWING IMAGE WITH OPEN CV
img = np.zeros((512, 512, 3), np.int8)

cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing', draw_rectangle)

while True:
    cv2.imshow('my_drawing', img)
    # if we wait 20 ms, and we've pressed the Esc
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
