import cv2


# CALLBACK FUNCTION RECTANGLE
def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, topLeft_clicked, bottomRight_clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        # RESET THE RECTANGLE (IT CHECKS IF THE RECT IS THERE)
        if topLeft_clicked and bottomRight_clicked:
            pt1 = (0, 0)
            pt2 = (0, 0)
            topLeft_clicked = False
            bottomRight_clicked = False
        if not topLeft_clicked:
            pt1 = (x, y)
            topLeft_clicked = True
        elif not bottomRight_clicked:
            pt2 = (x, y)
            bottomRight_clicked = True


# GLOBAL VARIABLES
pt1 = (0, 0)
pt2 = (0, 0)
topLeft_clicked = False
bottomRight_clicked = False

# CONNECT TO THE CALLBACK
cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle)

while True:
    ret, frame = cap.read()

    if topLeft_clicked:
        cv2.circle(frame, center=pt1, radius=5, color=(0, 0, 255), thickness=-1)

    if topLeft_clicked and bottomRight_clicked:
        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 3)
    # DRAW ON THE FRAME BASED ON THE GLOBAL VARIABLE

    cv2.imshow('Test', frame)

    if cv2.waitKey(10) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
