# tkinter Lesson 1

import tkinter as tk
from ctypes import windll

root = tk.Tk()

message = tk.Label(root, text="Hello, World!")
message.pack()

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()