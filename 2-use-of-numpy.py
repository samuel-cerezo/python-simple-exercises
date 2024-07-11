import cv2 as opencv
import random

#in opencv is BGR

img = opencv.imread('assets/zgz.jpg',opencv.IMREAD_COLOR)

print(img.shape)
#we print a pixel value in BGR at location (257,273)
print(img[257][273]) 

#we add some noise to the image and we save in another one
for raw in range(50):
   for column in range(img.shape[1]):
       img[raw][column] = [random.randint(0,255), random.randint(0,255), random.randint(0,255) ]


tag = img[100:200, 250:350]
img[200:300, 350:450] = tag

opencv.imshow('Titulo', img)
opencv.waitKey(5000)
opencv.destroyAllWindows()
