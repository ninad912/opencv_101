import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="zebra.jpg",
	help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original",image)
cv2.waitKey(0)

#addition operation to make the image brighter
M = np.ones(image.shape, dtype = "uint8")*100
bright = cv2.add(image,M)
cv2.imshow("Brighter",bright)
cv2.waitKey(0)

#subtraction operation to make the image darker
M = np.ones(image.shape, dtype = "uint8")*100
dark = cv2.subtract(image,M)
cv2.imshow("Darker",dark)
cv2.waitKey(0)

#image arithmetic using numpy subtraction
sub = image - M
cv2.imshow("Numpy Subtraction",sub)
cv2.waitKey(0)

