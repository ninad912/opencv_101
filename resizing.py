import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="dog.jpg",
	help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original",image)
cv2.waitKey(0)

#resizing the width to 200 pixels while maintaining the aspect ratio
r = 200 / image.shape[1]
dim = (200, int(image.shape[0]*r))

resized = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
cv2.imshow("Resized Width", resized)
cv2.waitKey(0)

#resizing the height to 100 pixels using imutils
resized = imutils.resize(image, height = 100)
cv2.imshow("Resized Height (Imutils)", resized)
cv2.waitKey(0)
 