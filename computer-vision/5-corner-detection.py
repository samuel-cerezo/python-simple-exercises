import numpy as np
import cv2

img = cv2.imread('assets/zgz.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
NumberOfCorners = 100
corners = cv2.goodFeaturesToTrack(gray, NumberOfCorners, 0.01, 10)
print(corners)  #we can see that this function shows float values
corners = np.int0(corners) #convert the corners to integerss
print(corners)  #we can see that this function shows float values

for i in corners:
    x,y = i.ravel() #delete the inner bracelets
    #we now draw the circle to mark the corner
    img = cv2.circle(img, (x,y), 5, (0,0,255),-1)

cv2.imshow('title', img)
cv2.waitKey(0)
cv2.destroyAllWindows()