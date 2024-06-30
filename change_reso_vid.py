import cv2 as cv
#reading videos

def change_res(capture,width,height):
    capture.set(3,width)
    capture.set(4,height)

capture =cv.VideoCapture(0)
width=640
height=480
change_res(capture,width,height)

while True:
    isTrue,frame=capture.read()  
    cv.imshow('Video',frame)
    if(cv.waitKey(20) &0xFF)==ord('d'):
        break
capture.release()
cv.destroyAllWindows()