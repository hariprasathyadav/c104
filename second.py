import cv2
import numpy as np
img = cv2.imread("poster.jpg")
#print(img)
rocket  = img[100:300,100:300]
cv2.imshow("rocket picture" , rocket)
cv2.waitKey(0)