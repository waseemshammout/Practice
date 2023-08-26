# tkinter Lesson 2

import tkinter as tk
from tkinter.messagebox import showinfo


root = tk.Tk()
root.title('Tkinter Window Demo')

# root.geometry('WidthxHeight+Left+Top') e.g. root.geometry('1000x400+150+10')

# Screen_Width = root.winfo_screenwidth()
# Screen_Height = root.winfo_screenheight()

# Window_Width = 600
# Window_Height = 400
# Window_Top = int((Screen_Height - Window_Height) / 2)
# Window_Left = int((Screen_Width - Window_Width) / 2)

# Geo = f'{Window_Width}x{Window_Height}+{Window_Left}+{Window_Top}'

root.geometry('1000x400+150+10')
# root.resizable(False,True) # allows resizing width & height

# root.minsize (100, 100)
# root.maxsize (800, 600)
# root.attributes('-alpha', 0.5)  # transparency of the window
# root.attributes('-topmost', 1) # stay on top
# Use lift() and lower() methods to move the window up and down of the window stacking order.
btn = tk.Button(root, text="Show me window title", command=lambda: showinfo('Data from Access', root.title())).pack()
root.iconbitmap('./favicon.ico')

root.mainloop()