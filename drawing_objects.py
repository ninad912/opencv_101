import numpy as np
import cv2

area = np.zeros((200, 200, 3), dtype = 'uint8')

r = (0,0,255)
g = (0,255,0)
b = (255,0,0)

#red line
cv2.line(area,(0,0),(200,200),r)
cv2.imshow('Drawings',area)
cv2.waitKey(0)

#blue line with thickness of 3 pixels
cv2.line(area,(200,0),(0,200),b,3)
cv2.imshow('Drawings',area)
cv2.waitKey(0)

#green square (50x50)
cv2.rectangle(area,(20,20),(70,70),g)
cv2.imshow('Drawings',area)
cv2.waitKey(0)

#green rectangle (60x40) with thickness fof 5 pixels
cv2.rectangle(area,(100,100),(160,140),g,5)
cv2.imshow('Drawings',area)
cv2.waitKey(0)

#filled green rectangle (20x40)
cv2.rectangle(area,(140,10),(160,50),g,-1)
cv2.imshow('Drawings',area)
cv2.waitKey(0)


#red concentric circles
for rad in range(0,100,10):
    cv2.circle(area,(100,100),rad,r)
    
cv2.imshow('Drawings',area)
cv2.waitKey(0)
    




    
