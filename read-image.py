import cv2 as cv

# Takes the path of an image and returns it as a matrix of pixels.
image = cv.imread('photos/drone.jpg')

# Display the image as a new window.
cv.imshow('Drone', image)

# Wait for keyboard key to exit the window.
cv.waitKey(0)
