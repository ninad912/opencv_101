import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="lebron_james.jpeg",
	help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#creating a  rectangular mask to show only the body
mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.rectangle(mask, (115, 5), (550, 413), 255, -1)
cv2.imshow("Mask",mask)
cv2.waitKey(0)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Masked Output",masked)
cv2.waitKey(0)

#creating a circular mask to show the face
mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.circle(mask, (280, 90), 50, 255, -1)
cv2.imshow("Mask",mask)
cv2.waitKey(0)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Masked Output",masked)
cv2.waitKey(0)