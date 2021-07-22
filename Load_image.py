from matplotlib import pyplot as plt
import argparse
import cv2

def plt_imshow(title, image):
	# convert the image frame BGR to RGB color space and display it
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	plt.imshow(image)
	plt.title(title)
	plt.grid(False)
	plt.show()
 
 args = {
	"image": "C:\Users\SPYDEN\Desktop\PyImageSearch Course\Lesson1\BUA_1.jpg",
}
 
 