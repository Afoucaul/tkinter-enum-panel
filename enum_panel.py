import tkinter as tk
from enum import Enum
from collections import OrderedDict


def to_label(text):
    return text


class EnumPanel(tk.Frame):
    def __init__(self, master, enum: Enum, orient=tk.VERTICAL):
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
            var.trace('w', self.on_option_clicked)
            self.buttons[k][1].pack(side=side, anchor="w")

    def on_option_clicked(self, *_):
        self.variable.set(True)

    def trace(self, callback):
        self.variable.trace('w', callback)

    def get(self):
        return [b[0] for b in self.buttons.values() if b[2].get()]

    def set(self, **checkedOptions):
        for k, v in self.buttons.items():
            if k in checkedOptions:
                v[2].set(checkedOptions[k])
