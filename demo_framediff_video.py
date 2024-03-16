# Background Subtraction using pybgs library
# This script demonstrates the usage of the pybgs library for background subtraction in a video.
# It processes a video file, extracts the moving objects by applying the FrameDifference algorithm,
# and displays the original video, the foreground mask, and the background model in real-time.

# Import necessary libraries
import numpy as np
import cv2
import pybgs as bgs

# Initialize the background subtraction algorithm
algorithm = bgs.FrameDifference()
video_file = "dataset/video.avi"

# Create a video capture object to read the video file
capture = cv2.VideoCapture(video_file)

# Wait for the video file to be opened
while not capture.isOpened():
  capture = cv2.VideoCapture(video_file)
  cv2.waitKey(1000)
  print("Waiting for the video to be loaded...")

# Main loop to process the video frames
while True:
  # Read a new frame
  flag, frame = capture.read()
  
  # If a frame was successfully read
  if flag:
    # Display the original video frame
    cv2.imshow('Original Video', frame)
    
    # Apply the background subtraction algorithm
    img_output = algorithm.apply(frame)
    # Retrieve the current background model
    img_bgmodel = algorithm.getBackgroundModel()
    
    # Display the foreground mask and the background model
    cv2.imshow('Foreground Mask', img_output)
    cv2.imshow('Background Model', img_bgmodel)
  else:
    # Wait for a bit and exit the loop if no frame is captured
    cv2.waitKey(1000)
    print("No more frames to read or error in reading the frame.")
    break
  
  # Break the loop if the user presses 'Esc'
  if cv2.waitKey(10) & 0xFF == 27:
    print("Exiting...")
    break

# Clean up: close all OpenCV windows and release the video capture object
cv2.destroyAllWindows()
capture.release()
