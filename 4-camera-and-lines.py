import numpy as np
import cv2

cap = cv2.VideoCapture(1) #access to the webcam

#loop until we press a key
while True:
    ret, frame = cap.read() #frame=image from the camera

    width = int(cap.get(3)) 
    height = int(cap.get(4))

    image = cv2.line(frame, (0,0), (width//3,height//2), (255,0,0),10)
    image = cv2.rectangle(image,(50,50),(100,100),(0,255,0),5)
    image = cv2.circle(image, (300,300), 60, (0,0,255),1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    image = cv2.putText(image,'Hallo Samu!',(10,height-10), font, 5, (0,0,0), 5)
    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release() #make the camera free to be used
cv2.destroyAllWindows()
