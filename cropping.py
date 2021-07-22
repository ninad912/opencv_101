import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="post_up.jpg",
	help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#cropping out Marc Gasol from input image
gasol = image[0:527, 77:448]
cv2.imshow("Marc Gasol", gasol)
cv2.waitKey(0)

#cropping out Nic Batum from input image
batum = image[68:527, 425:650]
cv2.imshow("Nic Batum",batum)
cv2.waitKey(0)

