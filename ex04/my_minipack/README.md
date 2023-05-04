# My MiniPack

## About this project

This package was made as a part of the Python02 module for the Cybersecurity bootcamp in 42 Barcelona. The main goal was to learn how to create and install a basic python package.  

## Package description
My MiniPack is a Python package that provides two modules: `progress` and `logger`. The `progress` module contains a `ft_progress` function that displays a progress bar in the console, while the `logger` module contains a `log` function that writes log messages to a file.

## Installation

To install My MiniPack, simply run:  
```bash build.sh```

## Usage

### Progress module

To use the `progress` module, you can import the `ft_progress` function as follows:

```python
from my_minipack.progress import ft_progress

for i in ft_progress(range(100)):
    # Do some work
```

This will display a progress bar in the console as the loop iterates. This function works with any kind of list and will yield each item.

### Logger module

To use the logger module, you can import the log function as follows:

```python
from my_minipack.logger import log

log("my_logger_name.log")
def function_to_be_logged:
    pass
```

The log function is a decorator that takes a string parameter to define the log file name. By default, it is named as logger.log. This example will write the log message to a file named "my_logger_name.log" in the current working directory.

## License

This package is released under the MIT license. For more information, see the LICENSE.md file.