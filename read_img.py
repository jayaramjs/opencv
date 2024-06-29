import cv2 as cv
#reading images
img=cv.imread('Photos/cat_large.jpg')
cv.imshow('cat',img)
cv.waitKey(0)

#reading videos
capture =cv.videocapture('videos//dog.mp4')
while True:
    isTrue,frame=capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) &0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()