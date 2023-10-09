from pynput import keyboard
try:
    from ib_exceptions import *
except:
    from interactive_buttons.ib_exceptions import *
import sys
_OUTPUT = None

# Define ANSI escape codes for highlighting and resetting text
class Variables:
    """
    Edit variables to customize selection menu.
    ANSI codes can be used with colorama Fore.
    """
    HIGHLIGHT = "\033[7m"  # Text/background color (defalut black on white)
    RESET = "\033[0m"
    SPACES = "     "  # Number of spaces between each buttons
    NEWLINE = "\n"
    DECORATOR = ["[", "]"]  # Decoration between each buttons


def column_buttons(buttons: dict, output=True):
    """
    Display colum buttons with highlighting and handle user input.
    Args:
        buttons (dict): A dictionary of button elements, each represented as a dict with the format:
            dict(name="nane", function=your_function, args=(your args if your function has arguments))
    Raises:
        ib_exceptions.MissingRequiredArgument: If a button element has less than 2 arguments.
        ib_exceptions.TooMuchArguments: If a button element has more than 3 arguments.
    """
    global highlighted_buttons, _OUTPUT
    highlighted_buttons = Variables.HIGHLIGHT  # Initialize with highlighting

    # Detecting if terminal is emulated
    if not sys.stdout.isatty():
        raise EmulatedTerminalDetected(
            "You are using an emulated terminal which means that colum function can't be used. Use 'linear_buttons' function instead.")

    # Loop through the list of buttons and validate their format
    for button_elements in buttons:
        if len(button_elements) < 2:
            raise ib_exceptions.MissingRequiredArgument("Missing arguments\nMust be ['button_name', 'function_name', 'function_arguments'=None]")
        elif len(button_elements) > 3:
            raise ib_exceptions.TooMuchArguments(
                "Useless arguments\nMust be ['button_name', 'function_name', 'function_arguments'=None]")

        # Highlight and add button names to the index string and check if button is diabled
        if len(Variables.DECORATOR) == 2:
            highlighted_buttons += f"{Variables.DECORATOR[0]}{button_elements['name']}{Variables.DECORATOR[1]}{Variables.RESET}{Variables.NEWLINE}"
        elif len(Variables.DECORATOR) == 1:
            highlighted_buttons += f"{Variables.DECORATOR[0]}{button_elements['name']}{Variables.RESET}{Variables.NEWLINE}"
        elif len(Variables.DECORATOR) == 0:
            highlighted_buttons += f"{button_elements['name']}{Variables.RESET}{Variables.NEWLINE}"
        else:
            raise ib_exceptions("Variables.DECORATOR length must be between 0 and 2 not more.")

    # Print the highlighted index string
    print(highlighted_buttons)

    def get_highlighted_index(button_list):
        """
        Get the index of the currently highlighted option.
        Args:
            button_list (list): A dictionary of button elements.
        Returns:
            int: Index of the currently highlighted option.
        """
        global highlighted_buttons

        for index, element in enumerate(button_list):
            if Variables.HIGHLIGHT in element:
                return index

    def change_highlighted_index(new_index_value):
        """
        Change the highlighted index.
        Args:
            new_index_value (int): The new index to highlight.
        """
        global highlighted_buttons

        cleaned_selector = highlighted_buttons.replace(Variables.HIGHLIGHT, "").replace(Variables.RESET, "")
        buttons_list = cleaned_selector.split(Variables.NEWLINE)

        index = buttons_list[new_index_value]

        buttons_list[new_index_value] = f"{Variables.RESET}{Variables.HIGHLIGHT}{index}{Variables.RESET}"

        highlighted_buttons = "\n".join(buttons_list)

        print(f"\033[{len(buttons) + 1}A\x1b[2K", end="")
        print(f"{highlighted_buttons}")

    def move_selection_up():
        """
        Move the selection index up.
        """
        global highlighted_buttons

        current_index = get_highlighted_index(highlighted_buttons.split(Variables.NEWLINE))
        if current_index - 1 < 0:
            change_highlighted_index(len(highlighted_buttons.split(Variables.NEWLINE)) - 2)
        else:
            change_highlighted_index(current_index - 1)

    def move_selection_down():
        """
        Move the selection index down.
        """
        global highlighted_buttons

        current_index = get_highlighted_index(highlighted_buttons.split(Variables.NEWLINE))
        if len(buttons) - 1 > current_index:
            change_highlighted_index(current_index + 1)
        else:
            change_highlighted_index(0)

    def execute_selected_function():
        """
        Execute the selected function.
        """
        global highlighted_buttons

        selected_index = get_highlighted_index(highlighted_buttons.split(Variables.NEWLINE))
        function_to_execute = buttons[selected_index]['function']
        print("\n", end="")

        # Check if the button has function arguments and execute accordingly
        try:
            args = buttons[selected_index]['args']
            if type(args) is tuple:
                return function_to_execute(*args)
            else:
                return function_to_execute(args)
        except KeyError:
            return function_to_execute()

        return True

    def on_key_press(key):
        """
        Handle keypress events.
        Args:
            key (keyboard.Key): The key that was pressed.
        """
        global highlighted_buttons, _OUTPUT

        if key == keyboard.Key.up:
            move_selection_up()
        elif key == keyboard.Key.down:
            move_selection_down()
        elif key == keyboard.Key.enter:
            _OUTPUT = execute_selected_function()
            return False

    # Start listening for keypress events
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

    if output is True:
        return _OUTPUT

def linear_buttons(buttons: dict, output=True):
    """
    Display linear buttons with highlighting and handle user input.
    Args:
        buttons (dict): A dictionary of button elements, each represented as a dict with the format:
            dict(name="nane", function=your_function, args=(your args if your function has arguments))
    Raises:
        ib_exceptions.MissingRequiredArgument: If a button element has less than 2 arguments.
        ib_exceptions.TooMuchArguments: If a button element has more than 3 arguments.
    """
    global highlighted_buttons, _OUTPUT
    highlighted_buttons = Variables.HIGHLIGHT  # Initialize with highlighting

    # Loop through the list of buttons and validate their format
    for button_elements in buttons:
        if len(button_elements) < 2:
            raise ib_exceptions.MissingRequiredArgument("Missing arguments\nMust be ['button_name', 'function_name', 'function_arguments'=None]")
        elif len(button_elements) > 3:
            raise ib_exceptions.TooMuchArguments(
                "Useless arguments\nMust be ['button_name', 'function_name', 'function_arguments'=None]")

        # Highlight and add button names to the index string and check if button is diabled
        if len(Variables.DECORATOR) == 2:
            highlighted_buttons += f"{Variables.DECORATOR[0]}{button_elements['name']}{Variables.DECORATOR[1]}{Variables.RESET}     "
        elif len(Variables.DECORATOR) == 1:
            highlighted_buttons += f"{Variables.DECORATOR[0]}{button_elements['name']}{Variables.RESET}     "
        elif len(Variables.DECORATOR) == 0:
            highlighted_buttons += f"{button_elements['name']}{Variables.RESET}     "
        else:
            raise ib_exceptions("Variables.DECORATOR length must be between 0 and 2 not more.")

    # Print the highlighted index string
    print(highlighted_buttons, end='', flush=True)

    def get_highlighted_index(button_list):
        """
        Get the index of the currently highlighted option.
        Args:
            button_list (list): A dictionary of button elements.
        Returns:
            int: Index of the currently highlighted option.
        """
        global highlighted_buttons

        for index, element in enumerate(button_list):
            if Variables.HIGHLIGHT in element:
                return index

    def change_highlighted_index(new_index_value):
        """
        Change the highlighted index.
        Args:
            new_index_value (int): The new index to highlight.
        """
        global highlighted_buttons

        cleaned_selector = highlighted_buttons.replace(Variables.HIGHLIGHT, "").replace(Variables.RESET, "")
        buttons_list = cleaned_selector.split(Variables.SPACES)

        index = buttons_list[new_index_value]

        buttons_list[new_index_value] = f"{Variables.RESET}{Variables.HIGHLIGHT}{index}{Variables.RESET}"

        highlighted_buttons = "     ".join(buttons_list)
        print(f"\r{highlighted_buttons}", end='', flush=True)

    def move_selection_backward():
        """
        Move the selection index backward.
        """
        global highlighted_buttons

        current_index = get_highlighted_index(highlighted_buttons.split(Variables.SPACES))
        if current_index - 1 < 0:
            change_highlighted_index(len(highlighted_buttons.split(Variables.SPACES)) - 2)
        else:
            change_highlighted_index(current_index - 1)

    def move_selection_forward():
        """
        Move the selection index forward.
        """
        global highlighted_buttons

        current_index = get_highlighted_index(highlighted_buttons.split(Variables.SPACES))
        if len(buttons) - 1 > current_index:
            change_highlighted_index(current_index + 1)
        else:
            change_highlighted_index(0)

    def execute_selected_function():
        """
        Execute the selected function.
        """
        global highlighted_buttons

        selected_index = get_highlighted_index(highlighted_buttons.split(Variables.SPACES))
        function_to_execute = buttons[selected_index]['function']
        print("\n", end="")

        # Check if the button has function arguments and execute accordingly
        try:
            args = buttons[selected_index]['args']
            if type(args) is tuple:
                return function_to_execute(*args)
            else:
                return function_to_execute(args)
        except KeyError:
            return function_to_execute()

        return True

    def on_key_press(key):
        """
        Handle keypress events.
        Args:
            key (keyboard.Key): The key that was pressed.
        """
        global highlighted_buttons, _OUTPUT

        if key == keyboard.Key.left:
            move_selection_backward()
        elif key == keyboard.Key.right:
            move_selection_forward()
        elif key == keyboard.Key.enter:
            _OUTPUT = execute_selected_function()
            return False

    # Start listening for keypress events
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

    if output is True:
        return _OUTPUT