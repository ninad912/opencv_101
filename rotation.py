import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="batman_logo.png",
	help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original",image)
cv2.waitKey()

#finding the center coordinates
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

#rotating 30 degrees anti-clockwise about the center
M = cv2.getRotationMatrix2D((cX,cY), 30, 1)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotation1",rotated)
cv2.waitKey(0)

#rotating 120 degrees clockwise about the center
M = cv2.getRotationMatrix2D((cX,cY), -120, 1)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotation2",rotated)
cv2.waitKey(0)

#rotating 45 degrees anti-clockwise about the (20,20)
M = cv2.getRotationMatrix2D((10, 10), 45, 1)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotation2",rotated)
cv2.waitKey(0)

#using imutils to rotate
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotation4",rotated)
cv2.waitKey(0)

#using imutils rotate_bound feature
rotated = imutils.rotate_bound(image, 30) 
cv2.imshow("Rotation4",rotated)
cv2.waitKey(0)