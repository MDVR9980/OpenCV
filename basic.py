import cv2 as cv

img = cv.imread('image/Cat.jpg')

cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)


# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# Dilating the image 
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize 
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Croping 
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)