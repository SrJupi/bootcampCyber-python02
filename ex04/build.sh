#!/bin/bash

# Upgrade pip and setuptools
pip install --upgrade pip -y
pip install --upgrade setuptools -y

# Install dependencies (wheel)
pip install -r requirements.txt -y

# Build package
cd my_minipack/
python setup.py sdist bdist_wheel

# Install package
pip install dist/*.whl
