import cv2

image = cv2.imread("butterfly.jpg")
print(image)
cv2.imshow("image1", image)
greyimage = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow("gray scaled image" , greyimage)
print(greyimage)
cv2.waitKey(0)