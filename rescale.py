import cv2 as cv

img = cv.imread('image/Cat.jpg')

cv.imshow('Cat', img)


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# def changeRes(width, height):
#     # Live video
#     capture.set(3, width)
#     capture.set(4, height)


resized_image = rescaleFrame(img, 0.25)
cv.imshow("Image", resized_image)
cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture('videos/ANIME.mkv')

while True:

    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame, 0.5)
    
    cv.imshow('Video', frame) 
    
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(1) & 0xFF == ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()