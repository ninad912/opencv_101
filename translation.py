import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="cars.jpg",
	help="path to the input image")
args = vars(ap.parse_args())

#showing the original image
image = cv2.imread(args["image"])
cv2.imshow('Original', image)
cv2.waitKey(0)

#translating left and down
M = np.float32([[1, 0, -30], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('Left and Down',shifted)
cv2.waitKey(0)

#translating right and up
M = np.float32([[1, 0, 30], [0, 1, -50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('Right and Up',shifted)
cv2.waitKey(0)