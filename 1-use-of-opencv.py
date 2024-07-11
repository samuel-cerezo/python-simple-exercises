import cv2 as opencv

# in opencv the RGB is BGR

img = opencv.imread('assets/zgz.jpg', opencv.IMREAD_COLOR)
#ways of loading the image: grayscale  - bgr
img = opencv.resize(img, (0,0),fx=0.5, fy=0.5)
opencv.imshow('Image',img)
opencv.waitKey(10000) #wait 10seconds = 10.000 miliseconds 
#wait for infinite amount of time
opencv.destroyAllWindows()