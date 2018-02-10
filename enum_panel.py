import tkinter as tk
from enum import Enum
from collections import OrderedDict
import re


def to_label(text: str) -> str:
    """Convert a camel case text into a nicer label"""
    return text[0].upper() + re.sub("([A-Z])", " \g<1>", text[1:]).lower()


class EnumPanel(tk.Frame):
    def __init__(self, master: tk.Misc, enum: Enum, orient=tk.VERTICAL):
        super().__init__(master)
        self.enum = enum
        self.variable = tk.BooleanVar()
        self.buttons = OrderedDict()

        if orient == tk.HORIZONTAL:
            side = tk.LEFT
        elif orient == tk.VERTICAL:
            side = tk.TOP
        else:
            raise ValueError("Unknown orientation: {}".format(orient))

        for k, v in self.enum.__members__.items():
            var = tk.IntVar()
            self.buttons[k] = (
                v, tk.Checkbutton(self, text=to_label(k), variable=var), var)
            var.trace('w', self._on_option_clicked)
            self.buttons[k][1].pack(side=side, anchor="w")

    def trace(self, callback) -> None:
        """Assign the given callback to a change of any of the options"""
        self.variable.trace('w', callback)

    def get(self) -> list:
        """Get the list of the enum members that are selected"""
        return [b[0] for b in self.buttons.values() if b[2].get()]

    def set(self, **checkedOptions: dict) -> None:
        """Set the specified options to either True or False"""
        for k, v in self.buttons.items():
            if k in checkedOptions:
                v[2].set(checkedOptions[k])

    def _on_option_clicked(self, *_):
        """Called when an option is clicked"""
        self.variable.set(True)
