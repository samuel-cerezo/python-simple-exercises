import numpy as np
import cv2

cap = cv2.VideoCapture(1) #access to the webcam

#loop until we press a key
while True:
    ret, frame = cap.read() #frame=image from the camera

    width = int(cap.get(3)) 
    height = int(cap.get(4))

    smaller_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    image = np.zeros(frame.shape, np.uint8)

    image[:height//2, :width//2] = smaller_frame
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release() #make the camera free to be used
cv2.destroyAllWindows()
