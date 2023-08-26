# tkinter Lesson 2

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Tkinter Window Demo')
root.iconbitmap('./favicon.ico')
# root.geometry('WidthxHeight+Left+Top')  e.g. root.geometry('1000x400+150+10')
# root.resizable(False,True) # allows resizing width & height
# root.minsize (100, 100)
# root.maxsize (800, 600)
# root.attributes('-alpha', 0.5)  # transparency of the window
# root.attributes('-topmost', 1) # stay on top
Screen_Width = root.winfo_screenwidth()
Screen_Height = root.winfo_screenheight()
Window_Width = 600
Window_Height = 400
Window_Top = int((Screen_Height - Window_Height) / 2)
Window_Left = int((Screen_Width - Window_Width) / 2)
Geo = f'{Window_Width}x{Window_Height}+{Window_Left}+{Window_Top}'
root.geometry(Geo)

# tk.Label(root, text='Classic Label').place(x=100, y=100)
# ttk.Label(root, text='Themed Label').place(x=200, y=200)

# ttk.Button(root, text='Button', command=lambda: print('Button')).pack()
# ttk.Checkbutton(root, text='Checkbutton', command=lambda: print('Checkbutton')).pack()
# ttk.Radiobutton(root, text='Radiobutton', value=1, command=lambda: print(1)).pack()
# ttk.Radiobutton(root, text='Radiobutton', value=2, command=lambda: print(2)).pack()
# ttk.Entry(root, textvariable='Hi').pack()
# ttk.Menubutton(root, text='Menubutton').pack()

# def button_clicked(name):
#     print('Printing ', name)

# button = ttk.Button(root, text='Click Me', command=lambda: button_clicked('Waseem')).place(x=10,y=15)

# def return_pressed(event):
#     print('Return Key Pressed!')

# def log(event):
#     print('Logged')

# def mouse_hover(event):
#     print('Mouse hovered over the label!')

# def print_entry_text(event):
#     print(textbox.get())

# btn = ttk.Button(root, text='Save')
# btn.bind('<Return>', return_pressed) # event 1
# btn.bind('<Return>', log, add='+')   # event 2
# btn.pack()

# ent = ttk.Entry(root)
# ent.bind('<Return>', return_pressed)
# ent.pack()

# label = ttk.Label(root, text='This is my label', font=("Roboto", 14))
# label.pack(ipadx=10, ipady=10)
# label.bind('<Enter>', mouse_hover)

# textbox = ttk.Entry(root, show='*')
# textbox.pack()
# textbox.bind('<Enter>', print_entry_text)

###########################################################################################

username = tk.StringVar()
password = tk.StringVar()

def signin(event):
    if username.get() == 'waseem' and password.get() == '123456':
        showinfo('Successfull login',
                 'You are logged in!')
    else:
        showinfo('Invalid credintials',
                 'Wrong username or password')

def signin_():
    if username.get() == 'waseem' and password.get() == '123456':
        showinfo('Successfull login',
                 'You are logged in!')
    else:
        showinfo('Invalid credintials',
                 'Wrong username or password')

lbl_username = ttk.Label(root, text='Username: ').place(x=10, y=10)
txt_username = ttk.Entry(root, textvariable=username).place(x=100, y=10)

lbl_password = ttk.Label(root, text='Password: ').place(x=10, y=50)
txt_password = ttk.Entry(root, textvariable=password, show='*')
txt_password.bind('<Return>', signin)
txt_password.place(x=100, y=50)

btn_login = ttk.Button(root, text='Sign In', command=signin_)
btn_login.place(x=10, y=90)

root.mainloop()
