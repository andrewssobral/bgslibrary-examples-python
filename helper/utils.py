"""
Utility Functions for Background Subtraction with pybgs Library

This script provides utility functions supporting the main demonstration of background subtraction
using various algorithms from the pybgs library. It includes OpenCV version checks, initialization
of a comprehensive list of background subtraction algorithms, and functions to process both video
files and image sequences using these algorithms.

Key Functions:
- is_cv2, is_cv3, is_cv4, is_lower_or_equals_cv347: Check the OpenCV version installed.
- check_opencv_version: Helper function to check for specific OpenCV major version.
- initialize_algorithms: Initializes a list of background subtraction algorithms available in the pybgs library, adjusted for the installed version of OpenCV.
- process_images: Processes a sequence of images using a specified background subtraction algorithm, displaying the original image, foreground mask, and background model.
- process_video: Processes video files frame by frame using a specified background subtraction algorithm, displaying the original frame, foreground mask, and background model.

Usage:
These utility functions are designed to be imported and used in a main script that demonstrates
the application of background subtraction techniques on video or image data. They handle the heavy
lifting of algorithm initialization and frame processing, simplifying the main script's logic.
"""

import cv2
import pybgs as bgs

# Functions to check OpenCV version
def is_cv2():
    return check_opencv_version("2.")

def is_cv3():
    return check_opencv_version("3.")

def is_lower_or_equals_cv347():
    [major, minor, revision] = cv2.__version__.split('.')
    return int(major) == 3 and int(minor) <= 4 and int(revision) <= 7

def is_cv4():
    return check_opencv_version("4.")

def check_opencv_version(major):
    return cv2.__version__.startswith(major)


def initialize_algorithms():
    """
    Initialize and return a list of background subtraction algorithms based on the installed OpenCV version.
    """
    algos = [
        bgs.FrameDifference(), bgs.StaticFrameDifference(), bgs.WeightedMovingMean(),
        bgs.WeightedMovingVariance(), bgs.AdaptiveBackgroundLearning(),
        bgs.AdaptiveSelectiveBackgroundLearning(), bgs.MixtureOfGaussianV2(),
        bgs.PixelBasedAdaptiveSegmenter(), bgs.SigmaDelta(), bgs.SuBSENSE(), bgs.LOBSTER(),
        bgs.PAWCS(), bgs.TwoPoints(), bgs.ViBe(), bgs.CodeBook(),
        bgs.FuzzySugenoIntegral(), bgs.FuzzyChoquetIntegral(), bgs.LBSimpleGaussian(),
        bgs.LBFuzzyGaussian(), bgs.LBMixtureOfGaussians(), bgs.LBAdaptiveSOM(),
        bgs.LBFuzzyAdaptiveSOM(), bgs.VuMeter(), bgs.KDE(), bgs.IndependentMultimodal()
    ]

    if is_cv2():
        algos.extend([bgs.MixtureOfGaussianV1(), bgs.GMG()])  # OpenCV 2.x specific

    if not is_cv2():
        algos.append(bgs.KNN())  # OpenCV > 2.x specific

    if is_cv2() or is_cv3():
        algos.extend([
            bgs.DPAdaptiveMedian(), bgs.DPGrimsonGMM(), bgs.DPZivkovicAGMM(),
            bgs.DPMean(), bgs.DPWrenGA(), bgs.DPPratiMediod(), bgs.DPEigenbackground(),
            bgs.DPTexture(), bgs.T2FGMM_UM(), bgs.T2FGMM_UV(), bgs.T2FMRF_UM(),
            bgs.T2FMRF_UV(), bgs.MultiCue()
        ])

    if is_cv2() or is_lower_or_equals_cv347():
        algos.extend([bgs.LBP_MRF(), bgs.MultiLayer()])

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
