import cv2 as cv

# Reading Images
img = cv.imread('image/Cat.jpg')

cv.imshow('Cat', img)


# Reading Videos
capture = cv.VideoCapture('videos/ANIME.mkv')

while True:

    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame) 
    
    cv.imshow('Video', frame)
    
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)