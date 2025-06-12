from pynput import keyboard
from colorama import Fore, Back, Style
import math


class Button:
    __slots__ = ("_label", "_value")

    def __init__(self, *, label: str, value: str):
        self._label = label
        self._value = value

    @property
    def label(self):
        return self._label

    @property
    def value(self):
        return self._value


class Component:
    def __init__(self, buttons,
                        text_color=Fore.BLACK,
                        highlight_color=Back.WHITE,
                        spaces_count=5,
                        left_decorator='[',
                        right_decorator=']'):
        self.buttons = buttons
        self.text_color = text_color
        self.highlight_color = highlight_color
        self.spaces_count = spaces_count
        self.left_decorator = left_decorator
        self.right_decorator = right_decorator


    @staticmethod
    def _clear_lines(n=1):
        for _ in range(n):
            print(f"\033[1A\x1b[2K", end="")

    def matrix_buttons(self):
        print("\n\n")
        btn_count = len(self.buttons)
        grid_size = math.ceil(math.sqrt(btn_count))
        x, y = 0, 0

        def print_matrix(sel_x=0, sel_y=0):
            self._clear_lines(grid_size)
            maxlen = max(len(b.label) for b in self.buttons)
            colw = maxlen + self.spaces_count
            out = ""
            for j in range(grid_size):
                for i in range(grid_size):
                    idx = j * grid_size + i
                    if idx >= btn_count:
                        break
                    btn = self.buttons[idx]
                    if (i, j) == (sel_x, sel_y):
                        out += f"{self.text_color}{self.highlight_color}{self.left_decorator}{btn.label}{self.right_decorator}{Style.RESET_ALL}"
                    else:
                        out += f"{self.left_decorator}{btn.label}{self.right_decorator}"
                    out += ' ' * (colw - len(btn.label) - 2)
                out += "\n"
            print(out, end="")

        def move(x, y, dx, dy):
            x = (x + dx) % grid_size
            y = (y + dy) % grid_size
            idx = y * grid_size + x
            if idx < btn_count:
                return x, y
            return 0, 0

        print_matrix(x, y)
        selected = {"value": None}

        def on_press(key):
            nonlocal x, y
            if key == keyboard.Key.right:
                x, y = move(x, y, 1, 0)
                print_matrix(x, y)
            elif key == keyboard.Key.left:
                x, y = move(x, y, -1, 0)
                print_matrix(x, y)
            elif key == keyboard.Key.up:
                x, y = move(x, y, 0, -1)
                print_matrix(x, y)
            elif key == keyboard.Key.down:
                x, y = move(x, y, 0, 1)
                print_matrix(x, y)
            elif key == keyboard.Key.enter:
                idx = y * grid_size + x
                selected["value"] = self.buttons[idx].value
                return False  # Stop listener

        with keyboard.Listener(on_press=on_press, suppress=True) as listener:
            listener.join()

        if selected["value"] is not None:
            return selected['value']
        else:
            return None
