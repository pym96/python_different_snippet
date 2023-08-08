# import cv2 as cv

''' 1. Reading photos'''
# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat',img)

''' 2. OpenCv can't read lagrer photos that bigger than our screen'''
# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat_large',img)


''' 3. Reading videos: Opencv will read video frame by frame, just that simple, this gonna be error since pytho couldn't find frame after the last frame'''
# capture = cv.VideoCapture('Videos/dog.mp4')
# while True:
#     isTrue,frame = capture.read()
#     cv.imshow('Video',frame)
    
#     if cv.waitKey(20) & 0xFF == ord('f'):
#         break

# capture.release()
# cv.destroyAllWindows()


''' 4. Resize and rescale frames: For photos and videos''' 

# capture = cv.VideoCapture('Videos/dog.mp4')
# def rescaleFrame(frame,scale = 0.75):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
    
#     dimensions = (width,height)
#     return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# while True:
#     isTrue,frame = capture.read()
#     frame_resized = rescaleFrame(frame,scale = .2)
#     cv.imshow('Video',frame_resized)

#     if cv.waitKey(20) & 0xFF == ord('f'):
#         break

# img = cv.imread('Photos/cat.jpg')
# img1 = rescaleFrame(img)
# cv.imshow('Cat',img1)
# cv.waitKey(0)

# capture.release()
# cv.destroyAllWindows()

''' 5. Resize photos: For live video, for those videos that files don't exist'''
# capture = cv.VideoCapture('Videos/dog.mp4')
# def changeRes(width,height):
#     capture.set(3,width) # 3 for width
#     capture.set(4,height) # 4 for height


''' 6. Drawing shapes and putting texts'''
# import cv2 as cv
# import numpy as np

# blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank',blank)

# blank[200:300,300:400] = 0,0,255
# cv.imshow('Blue',blank)

# # Chose all pixels 
# blank[:] = 0,255,0
# cv.imshow('Green',blank)

# Drawing a rectangle
# blank = np.zeros((500,500,3),dtype='uint8')
# blank = np.zeros((500,500,3),dtype='uint8')

# cv.rectangle(blank,(100,100),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)
# cv.imshow('rec',blank)

# Draw a circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,255,0),thickness=-3)
# cv.imshow('Circle',blank)

# Draw a line
# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
# cv.imshow('Line',blank)

# # Write text on imge
# cv.putText(blank,'Hello',(blank.shape[1]//2,blank.shape[0]//2),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,244,11),thickness=2)
# cv.imshow('Text',blank)

# cv.waitKey(0)

# This method allow our windos suspension : it'll waited for a infinite to wait for our keyboard input
# Just that simple
# cv.waitKey(0)

''' Convert img into gray scale'''
import cv2 as cv
img = cv.imread('Photos/park.jpg')

# gray_photo = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray_photo)

# # Blur
# blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

# canny Edge cascade
canny = cv.Canny(img,240,222)
cv.imshow('canny',canny)

# dilate the image
dilated = cv.dilate(canny,(3,3),iterations = 1)
cv.imshow('dilate',dilated)

# Eroding 
eroded = cv.erode(img,(2,2),iterations=3)
cv.imshow('eroded',eroded)

# Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

cv.imshow('orignal',img)



cv.waitKey(0)