import cv2 as cv

# A function that will resize the image.
def frame(frame, scale = 0.25):
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimensions = (width, height)

  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
