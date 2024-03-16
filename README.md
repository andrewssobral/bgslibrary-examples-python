# BGSlibrary Examples in Python

This repository contains Python scripts demonstrating the use of the `pybgs` library, a Python wrapper for the Background Subtraction Library (BGSlibrary). The examples illustrate how to apply different background subtraction algorithms on video data and image sequences for moving object detection.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg) ![Platform: Windows, Linux, OS X](https://img.shields.io/badge/Platform-Windows%2C%20Linux%2C%20OS%20X-blue.svg) ![OpenCV](https://img.shields.io/badge/OpenCV-2.4.x%2C%203.x%2C%204.x-blue.svg) ![Algorithms](https://img.shields.io/badge/Algorithms-43-red.svg)

[![BGS Library Demo](https://raw.githubusercontent.com/andrewssobral/bgslibrary/master/docs/images/bgs_giphy2.gif)](https://youtu.be/_UbERwuQ0OU)

## Features

- Demonstrations of various background subtraction algorithms from the `pybgs` library.
- Examples include processing both video files and image sequences.
- Usage of utility functions to simplify algorithm application and OpenCV version handling.

## Installation

To run the examples in this repository, you will need Python 3, OpenCV, NumPy, and the `pybgs` library. A virtual environment is recommended for managing the dependencies.

### Setting Up a Virtual Environment

You can set up a virtual environment and install the necessary dependencies by following these steps:

1. Clone the repository and navigate into it:

   ```bash
   git clone https://github.com/andrewssobral/bgslibrary-examples-python
   cd bgslibrary-examples-python
   ```

2. Run the `virtualenv.sh` script to create a virtual environment and install dependencies:

   ```bash
   ./virtualenv.sh
   ```

This script will create a new virtual environment named `env`, upgrade pip, and install `numpy`, `opencv-python`, and `pybgs`.

## Usage

There are several demonstration scripts included in the repository:

- `demo_framediff_video.py`: Demonstrates the Frame Difference algorithm on a video file.
- `demo_multi_bgs.py`: An advanced demonstration processing video files or image sequences with multiple background subtraction algorithms.
- `demo_list_algs.py`: Lists all the background subtraction algorithms available in the pybgs library with their index numbers.
- `demo_show_version.py`: Displays the currently installed version of the pybgs library.

To run an example, make sure your virtual environment is activated, and then execute the script like so:

```bash
python demo_framediff_video.py
```

Replace `demo_framediff_video.py` with the name of the script you wish to run.

## Additional Notes

- Make sure to place your video files or image sequences in the appropriate directory as specified by the scripts (`dataset/video.avi` for videos, `dataset/frames` for image sequences).
- The `helper/utils.py` script contains utility functions used by the demonstration scripts. Ensure this script is accessible by placing it in a `helper` directory within your project.

## Google Colab example

Please click on the link below to access the notebook example on Google Colab:

https://colab.research.google.com/drive/1HDc0cE7PDQM9zxm5z-bK_UggzIBpK2DH

The same notebook is available under the folder `notebooks`.

## Acknowledgements

This project utilizes the `pybgs` library, a Python wrapper for the BGSlibrary, to demonstrate background subtraction techniques.

## License

MIT License
