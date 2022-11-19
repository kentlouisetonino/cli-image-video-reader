import cv2 as cv

image = cv.imread('photos/drone.jpg') # Takes the path of an image and returns it as a matrix of pixels.

cv.imshow('Drone', image) # Display the image as a new window.
cv.waitKey(0)
