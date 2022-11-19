import cv2 as cv

# You can pass integer (0/1/2) which will represent your machine webcam.
videoCapture = cv.VideoCapture('videos/video1.mp4')

while True:
  # Read the video frame by frame.
  isTrue, frame = videoCapture.read()

  # Display an individual frame.
  cv.imshow('Video', frame) 
  
  # Stop the video from playing indefinitely.
  if cv.waitKey(20) & 0xFF == ord('d'):
    break

# Release the capture pointer.
videoCapture.release()

# Destroy all windows.
cv.destroyAllWindows()
