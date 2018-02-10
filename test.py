import tkinter as tk
from enum import Enum
from enum_panel import EnumPanel


class Foo(Enum):
    FirstValue = 1
    SecondValue = 2
    ThirdValue = 3


if __name__ == '__main__':
    def callback(*_):
        print(panel.get())

    root = tk.Tk()
    panel = EnumPanel(root, Foo)
    panel.pack()

    panel.trace(callback)
    panel.set(FirstValue=True, ThirdValue=True)

    root.mainloop()
