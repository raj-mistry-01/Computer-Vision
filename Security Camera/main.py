import cv2
import winsound
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True : 
    _,frame1 = cam.read()
    _,frame2 = cam.read()
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray,20,255,cv2.THRESH_BINARY)
    cv2.imshow("Security Camera",thresh)
    contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours : 
        if cv2.contourArea(c) < 1000 :
            continue
        winsound.Beep(450,100)
    k =cv2.waitKey(100) & 0xff 
    if k==27: 
        break # press escape to close the camera

