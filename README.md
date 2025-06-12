# Interactive Buttons Library

A Python library to create interactive buttons with keyboard navigation.

---

## 📦 Installation

```bash
pip install interactive_buttons
```

---

## ⚙️ Features

* Buttons displayed as a **matrix**.
* Navigation using arrow keys (`↑ ↓ → ←`).
* Selection using the **Enter** key.
* Customization of colors, spacing, and decorators.

---

## 🧪 Example usage of `matrix_buttons`

```python
from interactive_buttons import Button, Component
from colorama import Fore, Back

# Create buttons
buttons = [
    Button(label="A1", value="Value A1"),
    Button(label="A2", value="Value A2"),
    Button(label="B1", value="Value B1"),
    Button(label="B2", value="Value B2"),
]

# Create custom component
component = Component(
    buttons=buttons,
    text_color=Fore.BLACK,
    highlight_color=Back.YELLOW,
    spaces_count=6,
    left_decorator="<",
    right_decorator=">"
)

# Launch the interactive interface
value = component.matrix_buttons()

# Display the selected value
print(f"Selected value: {value}")
```

### 🎯 Expected result

* Buttons are displayed in a grid.
* The user navigates with the arrow keys.
* When a button is selected (by pressing **Enter**), its `value` is returned and displayed.

### Output Example : 

![](https://github.com/mbcraft-exe/interactive_buttons/blob/main/assets/asset%20v4.png)

---

## ❗ Requirements

* Do **not use** an emulated terminal (such as VS Code integrated terminal or online consoles): they prevent correct keyboard input capture.
* The library depends on:

  * [`pynput`](https://pypi.org/project/pynput/)
  * [`colorama`](https://pypi.org/project/colorama/)

---

## 📄 Project description

**Interactive Buttons** allows you to create interactive text-based menus. It’s a simple solution for:

* command-line interfaces,
* interactive terminal tools,
* user tests or step-by-step assistants.

---

## 🔗 GitHub Repository

Check the GitHub repository for updates and contributions:

👉 [https://github.com/mbcraft-exe/interactive\_buttons](https://github.com/mbcraft-exe/interactive_buttons)
