import tkinter as tk
from tkinter import Menu
from tkinter.messagebox import showinfo


class StatusBar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.variable = tk.StringVar()
        self.label = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W,
                              textvariable=self.variable,
                              font=('Tahoma', 8, 'normal'))
        self.variable.set('Status Bar')
        self.label.pack(fill=tk.X)
        self.pack(ipadx=root.winfo_screenwidth(), ipady=root.winfo_height())


root = tk.Tk()
root.title('Pack Demo')
root.geometry("350x200")

menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(
    label='Show Message',
    command=lambda: showinfo('Title', 'Message Box Test'))
file_menu.add_command(
    label='Exit',
    command=lambda: root.quit())

edit_menu = Menu(menubar, tearoff=False)
edit_menu.add_command(
    label='Cut',
    command=lambda: showinfo('Title', 'Cut pressed'))
edit_menu.add_command(
    label='Copy',
    command=lambda: showinfo('Title', 'Copy pressed'))
edit_menu.add_command(
    label='Paste',
    command=lambda: showinfo('Title', 'Paste pressed'))

menubar.add_cascade(label='File', menu=file_menu, underline=0)
menubar.add_cascade(label='Edit', menu=edit_menu, underline=0)
# box 1
box1 = tk.Label(root, text="Box", bg="green", fg="white")
box1.pack(ipadx=10)
d = StatusBar(root)
root.state('zoomed')
root.mainloop()
