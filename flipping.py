import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="slam_dunk.jpg",
	help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#flipping horizontally
flipped = cv2.flip(image,1)
cv2.imshow("Horizontal Flip",flipped)
cv2.waitKey(0)

#flipping verically
flipped = cv2.flip(image,0)
cv2.imshow("Verical Flip",flipped)
cv2.waitKey(0)

#flipping both ways
flipped = cv2.flip(image,-1)
cv2.imshow("Flipped Both Ways",flipped)
cv2.waitKey(0)