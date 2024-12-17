import cv2 as cv
import os
import re_scale

# Takes the path of an image and returns it as a matrix of pixels.
file_path = os.path.join(os.path.dirname(__file__), 'files/image.jpg')
image = cv.imread(file_path)

print(image.shape)

# Resized the image to 25% smaller.
resized_frame = re_scale.frame(image)

# Display the image as a new window.
cv.imshow('Drone', resized_frame)

# Wait for keyboard key to exit the window.
cv.waitKey(0)
