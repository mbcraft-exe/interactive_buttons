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

# Change button color :
# Way 1 :
linear_buttons.Variables.HIGHLIGHT = "\033[30;43m"  # Yellow background
# Way 2 :
from colorama import Fore, Back  # Needs to be installed by running the command `pip install colorama`
linear_buttons.Variables.HIGHLIGHT = Back.RED + Fore.BLACK  # Red background and Black text

# Change decorator (in [button text] the square brackets are the decorators) :
# Way 1 :
linear_buttons.Variables.DECORATOR = ["<", ">"]  # [button text] -> <button text>
# Way 2 :
linear_buttons.Variables.DECORATOR = []  # [button text] -> button text
# Way 3 :
linear_buttons.Variables.DECORATOR = ["> "]  # [button text] ->  > button text



# Define button configurations as a list
button_configurations = [
    ['Button 1', function_1],
    ['Button 2', function_2, ('arg1', 'arg2')],
]

# Create linear buttons and start the interactive interface
linear_buttons(button_configurations)
```
### Output examples 
![](https://cdn.discordapp.com/attachments/946745366395621379/1160349182255710248/image.png?ex=65345663&is=6521e163&hm=bd800369153eabe30b340cfee3ede6a4002dcb630218a8ffe1245e7f40201e16&)


## Project Description

The Interactive Buttons library allows you to easily create interactive buttons for user interaction in your Python applications. It provides a simple and intuitive way to create a list of buttons, associate them with functions, and navigate through them using the keyboard. This library is particularly useful for creating text-based interactive menus and interfaces.

## PyPi Repository

Check out the [PyPi repository](https://pypi.org/project/interactive-buttons/) for the latest update !
