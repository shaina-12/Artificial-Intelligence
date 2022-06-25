# Code to Access Camera

import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    check, frame = cam.read()
    # if frame is read correctly ret is True
    if not check:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Display the resulting frame
    cv2.imshow('video',frame)
    key = cv2.waitKey(1)
    if (key==27):
        break
# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()