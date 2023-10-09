# Interactive Buttons Library

A Python library for creating interactive buttons with keyboard navigation.

## Installation

You can install the Interactive Buttons library via pip:

```bash
pip install interactive_buttons
```


## Usage

#### Here's an example of how to use the library to create interactive buttons with `linear_buttons` :

```python
from interactive_buttons import *
from colorama import Fore, Back

# Change button color :
# Way 1 :
Variables.HIGHLIGHT = "\033[30;43m"  # Yellow background
# Way 2 :
from colorama import Fore, Back  # Needs to be installed by running the command `pip install colorama`
Variables.HIGHLIGHT = Back.RED + Fore.BLACK  # Red background and Black text

# Change decorator (in [button text] the square brackets are the decorators) :
# Way 1 :S
Variables.DECORATOR = ["<", ">"]  # [button text] -> <button text>
# Way 2 :
Variables.DECORATOR = []  # [button text] -> button text
# Way 3 :
Variables.DECORATOR = ["> "]  # [button text] ->  > button text

# Creating functions
def func1(text):
    print(text)

def func2():
    print("Hi !")

# Define button configurations as a list
buttons = [dict(name="Button 1", function=func1, args=("Hello !")),
           dict(name="Button 2", function=func2)]

# Create linear buttons and start the interactive interface
linear_buttons(buttons)
```
### Output example 
![](https://cdn.discordapp.com/attachments/946745366395621379/1160349182255710248/image.png?ex=65345663&is=6521e163&hm=bd800369153eabe30b340cfee3ede6a4002dcb630218a8ffe1245e7f40201e16&)


#### Example with `column_buttons` :
### ⚠️ WARNING : To use this function, you must not use an emulated terminal.

```python
from interactive_buttons import *

# Creating functions
def func1(text):
    print(text)

def func2():
    print("Hi !")

# Define button configurations as a list
buttons = [dict(name="Button 1", function=func1, args=("Hello !")),
           dict(name="Button 2", function=func2),
           dict(name="Button 3", function=func1, args=("Hello2 !")),
           dict(name="Button 4", function=func2),]

# Create column buttons and start the interactive interface
column_buttons(buttons)
```

### Output example 
![](https://cdn.discordapp.com/attachments/946745366395621379/1161044163450650814/image.png?ex=6536dda3&is=652468a3&hm=c6fbbeb849d612a77e98fd798df56cc65536575a096f8ae8b27e1f5d402583d0&)

## Project Description

The Interactive Buttons library allows you to easily create interactive buttons for user interaction in your Python applications. It provides a simple and intuitive way to create a list of buttons, associate them with functions, and navigate through them using the keyboard. This library is particularly useful for creating text-based interactive menus and interfaces.

## GitHub Repository

Check out the [GitHub repository](https://github.com/mbcraft-exe/interactive_buttons) for the latest updates, issues, and contributions. Feel free to contribute to the project or report any issues you encounter.
