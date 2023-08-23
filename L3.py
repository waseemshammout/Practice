# tkinter Lesson 3

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import pyodbc

root = tk.Tk()
root.geometry('1000x400+150+10')
root.iconbitmap('./favicon.ico')


def callBack():
    root.geometry('10x10+50+50')


def download_clicked():
    showinfo(
        title='Information',
        message='Download Completed!'
    )


def show_crypto():
    conn = pyodbc.connect(
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Waseem\Desktop\Python\crypto_database.accdb;"
    )
    cursor = conn.cursor()
    cursor.execute('Select * from crypto_table')
    for row in cursor.fetchall():
        showinfo(
            title='Data from Access',
            message=row[1]
        )


button = ttk.Button(root, text='Show Crypto', command=show_crypto)
button.state(['!disabled'])
button.pack(padx=10, pady=20)

exit_button = ttk.Button(root, text='Exit', state=[
                         '!disabled'], command=lambda: root.quit()).pack(padx=10, pady=20)

download_icon = tk.PhotoImage(file='./download.png')
download_button = ttk.Button(root, image=download_icon, text='Download',
                             compound=tk.LEFT, command=download_clicked).pack(padx=10, pady=20)

root.mainloop()
