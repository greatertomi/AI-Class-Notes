import cv2
import time

cap = cv2.VideoCapture('mysupervideo.mp4')

if cap.isOpened() == False:
    print('Error: File not found or wrong CODEC used')

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        time.sleep(1 / 20)  # This slows down the video play so that it is not fast
        cv2.imshow('frame', frame)
        if cv2.waitKey(10) & 0XFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
