# BGSlibrary Examples in Python

This repository contains Python scripts demonstrating the use of the `pybgs` library, a Python wrapper for the Background Subtraction Library (BGSlibrary). The examples illustrate how to apply different background subtraction algorithms on video data and image sequences for moving object detection.

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

- `demo_framediff_video.py`: Shows how to use the Frame Difference algorithm on a video file.
- `demo_multi_bgs.py`: An advanced demonstration that processes video files or image sequences with multiple background subtraction algorithms.
- `demo_show_version.py`: Displays the version of the `pybgs` library.

To run an example, make sure your virtual environment is activated, and then execute the script like so:

```bash
python demo_framediff_video.py
```

Replace `demo_framediff_video.py` with the name of the script you wish to run.

## Additional Notes

- Make sure to place your video files or image sequences in the appropriate directory as specified by the scripts (`dataset/video.avi` for videos, `dataset/frames` for image sequences).
- The `helper/utils.py` script contains utility functions used by the demonstration scripts. Ensure this script is accessible by placing it in a `helper` directory within your project.

## Acknowledgements

This project utilizes the `pybgs` library, a Python wrapper for the BGSlibrary, to demonstrate background subtraction techniques.

## License

MIT License
