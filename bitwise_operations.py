import numpy as np
import cv2

#drawing a binary images of a rectangle
rectangle = np.zeros((500, 500), dtype = "uint8")
cv2.rectangle(rectangle, (40, 40), (460, 460), 255, -1)
cv2.imshow("Rectangle",rectangle)

#drawing a binary images of a circle
circle = np.zeros((500, 500), dtype = "uint8")
cv2.circle(circle, (250, 250), 250, 255, -1)
cv2.imshow("Circle", circle)

cv2.waitKey(0)

#bitwise AND operation on the images
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

#bitwise OR operation on the images
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

##bitwise NOT operation on the rectangle
bitwiseNot = cv2.bitwise_not(rectangle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)