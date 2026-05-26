"""
Utility Functions for Background Subtraction with pybgs Library

This script provides utility functions supporting the main demonstration of background subtraction
using various algorithms from the pybgs library. It includes OpenCV version checks, initialization
of a comprehensive list of background subtraction algorithms, and functions to process both video
files and image sequences using these algorithms.

Key Functions:
- initialize_algorithms: Instantiates the background subtraction algorithms exposed by the installed pybgs build (each added only if available; see the note in the function).
- process_images: Processes a sequence of images using a specified background subtraction algorithm, displaying the original image, foreground mask, and background model.
- process_video: Processes video files frame by frame using a specified background subtraction algorithm, displaying the original frame, foreground mask, and background model.

Usage:
These utility functions are designed to be imported and used in a main script that demonstrates
the application of background subtraction techniques on video or image data. They handle the heavy
lifting of algorithm initialization and frame processing, simplifying the main script's logic.
"""

import cv2
import pybgs as bgs

def initialize_algorithms():
    """
    Instantiate and return the background subtraction algorithms exposed by the
    installed pybgs build.

    Which algorithms are available depends on the OpenCV version pybgs was COMPILED
    against, not on cv2.__version__ (the opencv-python build). We therefore instantiate
    each one only if this pybgs build exposes it, skipping the rest with a message, so
    the demos work with any build instead of raising AttributeError.
    """
    names = [
        # Available on all supported OpenCV versions
        "FrameDifference", "StaticFrameDifference", "WeightedMovingMean",
        "WeightedMovingVariance", "AdaptiveBackgroundLearning",
        "AdaptiveSelectiveBackgroundLearning", "MixtureOfGaussianV2",
        "PixelBasedAdaptiveSegmenter", "SigmaDelta", "SuBSENSE", "LOBSTER",
        "PAWCS", "TwoPoints", "ViBe", "CodeBook",
        "FuzzySugenoIntegral", "FuzzyChoquetIntegral", "LBSimpleGaussian",
        "LBFuzzyGaussian", "LBMixtureOfGaussians", "LBAdaptiveSOM",
        "LBFuzzyAdaptiveSOM", "VuMeter", "KDE", "IndependentMultimodal",
        # OpenCV 2.x only
        "MixtureOfGaussianV1", "GMG",
        # OpenCV > 2.x
        "KNN",
        # OpenCV 2.x / 3.x only
        "DPAdaptiveMedian", "DPGrimsonGMM", "DPZivkovicAGMM", "DPMean", "DPWrenGA",
        "DPPratiMediod", "DPEigenbackground", "DPTexture",
        "T2FGMM_UM", "T2FGMM_UV", "T2FMRF_UM", "T2FMRF_UV", "MultiCue",
        # OpenCV 2.x / <= 3.4.7 only
        "LBP_MRF", "MultiLayer",
    ]

    algos = []
    for name in names:
        if hasattr(bgs, name):
            algos.append(getattr(bgs, name)())
        else:
            print("skipping (not available in this pybgs build):", name)
    return algos

def process_images(img_array, algorithm):
    """
    Process each image in img_array with the specified algorithm.
    Displays original image, foreground mask, and background model.
    """
    for img_path in img_array:
        img = cv2.imread(img_path)
        img_output = algorithm.apply(img)
        img_bgmodel = algorithm.getBackgroundModel()

        cv2.imshow('Original Image', img)
        cv2.imshow('Foreground Mask', img_output)
        cv2.imshow('Background Model', img_bgmodel)

        if cv2.waitKey(10) & 0xFF == 27:  # Exit if ESC is pressed
            break

        print("Frames left: " + str(len(img_array) - img_array.index(img_path)))

def process_video(video_file, algorithm):
    """
    Process each frame of the specified video file with the given algorithm.
    Displays original video frame, foreground mask, and background model.
    """
    capture = cv2.VideoCapture(video_file)
    while not capture.isOpened():
        capture = cv2.VideoCapture(video_file)
        cv2.waitKey(1000)
        print("Waiting for the video to be loaded...")

    while True:
        flag, frame = capture.read()
        if not flag:
            # print("No more frames to read or error in reading the frame.")
            break

        cv2.imshow('Original Video', frame)
        img_output = algorithm.apply(frame)
        img_bgmodel = algorithm.getBackgroundModel()

        cv2.imshow('Foreground Mask', img_output)
        cv2.imshow('Background Model', img_bgmodel)

        if cv2.waitKey(10) & 0xFF == 27:  # Exit if ESC is pressed
            break
