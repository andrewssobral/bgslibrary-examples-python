import cv2
from helper.utils import *

# Display the installed OpenCV version
print("OpenCV Version: {}".format(cv2.__version__))

# Initialize available algorithms based on the OpenCV version
algorithms = initialize_algorithms()

# Notify the user about the number of algorithms initialized
print("Number of available algorithms: ", len(algorithms))

# List the available algorithms with their index numbers
for index, algorithm in enumerate(algorithms, start=1):  # start=1 begins counting from 1 instead of 0
    print(f"{index}: {type(algorithm).__name__}")
