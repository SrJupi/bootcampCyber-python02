from setuptools import setup, find_packages

setup(
    name="my_minipack",
    version="1.0.0",
    description="How to create a package in python.",
    author="Lucas Sulzbach Rilho",
    author_email="lsulzbac@student.42barcelona.com",
    url="https://github.com/SrJupi",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Students",
        "Topic :: Education",
        "Topic :: HowTo",
        "Topic :: Package",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_packages(),
)