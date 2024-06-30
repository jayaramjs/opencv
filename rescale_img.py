import cv2 as cv
#reading images
img=cv.imread('Photos/cat_large.jpg')
def rescale_frame(frame,scale=0.2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
image=rescale_frame(img)
cv.imshow('cat',image)
cv.waitKey(0)
