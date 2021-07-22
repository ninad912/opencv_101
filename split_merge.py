import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="opencv_logo.png",
	help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#splitting the image into its RGB channels
(B, G, R) = cv2.split(image)

cv2.imshow("RED", R)
cv2.imshow("GREEN", G)
cv2.imshow("BLUE", B)
cv2.waitKey(0)

#merging the images back together
merged = cv2.merge([B, G, R])
cv2.imshow("Merged Image", merged)
cv2.waitKey(0)
