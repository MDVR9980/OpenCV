import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')
cv.imshow('Blank', blank)

img = cv.imread('image/Cat.jpg')
cv.imshow('Cat', img)

# 1. Paint the image a certain colour
blank[200:300, 0:500] = 255, 0, 0
cv.imshow('Green', blank)

# 2. Draw a Rectangle 
cv.rectangle(blank, (0, 0), (500, 250),(0, 255, 0), thickness=-1)
cv.rectangle(blank,(0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)

cv.rectangle(blank,(0, 0), ((blank.shape[1]//2), (blank.shape[0]//2)), (0, 255, 0), thickness=-1)
cv.rectangle(blank,(0, 250), ((blank.shape[1]//2), (blank.shape[0]//2) + 250), (255, 0, 0), thickness=-1)
cv.rectangle(blank,(250, 0), ((blank.shape[1]//2) + 250, (blank.shape[0]//2)), (0, 0, 255), thickness=-1)
cv.rectangle(blank,(250, 250), ((blank.shape[1]//2) + 250, (blank.shape[0]//2) +250), (12, 24, 120), thickness=-1)

cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED)  # Green  
cv.rectangle(blank, (0, 250), (250, 500), (255, 0, 0), thickness=cv.FILLED)  # Red  
cv.rectangle(blank, (250, 0), (500, 250), (0, 0, 255), thickness=cv.FILLED)  # Blue  
cv.rectangle(blank, (250, 250), (500, 500), (120, 240, 120), thickness=cv.FILLED)  # Light Green  

# cv.imshow('Rectangle', blank)


# 3. draw A circle 
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.line(blank, (125, 250), (375, 250), (255, 255, 255), thickness=3)
cv.line(blank, (250, 125), (250, 375), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is David', (25,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)