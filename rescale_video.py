import cv2 as cv

def rescale_frame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

capture =cv.VideoCapture('videos//dog.mp4')
while True:
    isTrue,frame=capture.read()
    frame2=rescale_frame(frame)
    cv.imshow('Video',frame2)
    if(cv.waitKey(20) &0xFF)==ord('d'):
        break
capture.release()
cv.destroyAllWindows()