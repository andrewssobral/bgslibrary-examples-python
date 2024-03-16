# Remove the existing virtual environment if it exists
rm -rf env

# Create a new virtual environment called env using Python3
python3 -m venv env

# Activate the newly created virtual environment
source env/bin/activate

# Upgrade pip and install required packages numpy and OpenCV
python -m pip install --upgrade pip
python -m pip install wheel setuptools
python -m pip install numpy
python -m pip install opencv-python

# Install pybgs (bgslibrary python wrapper)
python -m pip install pybgs
