# Interactive Buttons Library

A Python library for creating interactive buttons with keyboard navigation.

## Installation

You can install the Interactive Buttons library via pip:

```bash
pip install interactive_buttons
```


## Usage

Here's an example of how to use the library to create interactive buttons:

```python
from interactive_buttons import linear_buttons

# Define button configurations as a list
button_configurations = [
    ['Button 1', function_1],
    ['Button 2', function_2, ('arg1', 'arg2')],
]

# Create linear buttons and start the interactive interface
linear_buttons(button_configurations)
```

## Project Description

The Interactive Buttons library allows you to easily create interactive buttons for user interaction in your Python applications. It provides a simple and intuitive way to create a list of buttons, associate them with functions, and navigate through them using the keyboard. This library is particularly useful for creating text-based interactive menus and interfaces.

## PyPi Repository

Check out the [PyPi repository](https://pypi.org/project/interactive-buttons/) for the latest update !
