import cv2
image = cv2.imread("image.jpg")
small = cv2.resize(image,(300,200))
medium = cv2.resize(image,(400,500))
large = cv2.resize(image,(800,800) )

cv2.imshow("small image" , small)
cv2.imshow("medium image" , medium)
cv2.imshow("large image" , large)

cv2.imwrite("small_image.jpg" ,small)
cv2.imwrite("medium_image.jpg" , medium)
cv2.imwrite("large_image.jpg" , large)

cv2.WaitKey(0)
cv2.destroyAllWindows()