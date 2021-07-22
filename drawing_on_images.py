import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="cars.jpg",
	help="path to the input image")
args = vars(ap.parse_args())

#loading thr image
image = cv2.imread(args['image'])

#drawing a box (thicknes of 3 pixels) over a car
red = (0,0,255)
cv2.rectangle(image,(119,186),(475,424),red,3)

cv2.imshow('OUTPUT',image)
cv2.waitKey(0)

