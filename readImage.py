import cv2 as cv

import reScale

# Takes the path of an image and returns it as a matrix of pixels.
image = cv.imread('photos/drone.jpg')


# Resized the image to 25% smaller.
resized_frame = reScale.frame(image)

# Display the image as a new window.
cv.imshow('Drone', resized_frame)

# Wait for keyboard key to exit the window.
cv.waitKey(0)
