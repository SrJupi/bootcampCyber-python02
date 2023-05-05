#!/bin/bash

# Upgrade pip and setuptools
pip install --upgrade pip
pip install --upgrade setuptools

# Install dependencies (wheel)
pip install -r requirements.txt

# Build package
cd my_minipack/
python setup.py sdist bdist_wheel

# Install package
pip install dist/*.whl
