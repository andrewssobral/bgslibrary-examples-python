"""
List Background Subtraction Algorithms

This script lists all the background subtraction algorithms available in the pybgs library.
It demonstrates how to initialize the algorithms and then print each one with its corresponding index number.

Requirements:
- OpenCV
- pybgs library
"""

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
