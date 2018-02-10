# tkinter-enum-panel

This TkInter class helps displaying a graphical representation of an enumeration type, through a panel of checkbuttons.

## Example

### Complete code using the `EnumPanel` class

    import tkinter as tk
    from enum_panel import EnumPanel
    from enum import Enum
    

    class MyEnum(Enum):
        FirstValue = 1
        SecondValue = 2
        ThirdValue = 3


    root = tk.Tk()
    panel = EnumPanel(root, MyEnum)
    panel.pack()
    root.mainloop()

### Visual output (approximation)

    ___________________
    |                 |
    | 口 First value  |
    |                 |
    | 口 Second value |
    |                 |
    | 口 Third value  |
    |_________________|
