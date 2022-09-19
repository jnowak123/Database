import tkinter as tk
import random

def uptade1():
    b1.configure(text='X')

def uptade2():
    b2.configure(text='X')

def uptade3():
    b3.configure(text='X')

def uptade4():
    b4.configure(text='X')

def uptade5():
    b5.configure(text='X')

def uptade6():
    b6.configure(text='X')

def uptade7():
    b7.configure(text='X')

def uptade8():
    b8.configure(text='X')

def uptade9():
    b9.configure(text='X')


window = tk.Tk()
b1 = tk.Button(text='', height = 15, width = 39, bg='Black', fg='White', command=uptade1)
b2 = tk.Button(text='', height = 15, width = 39, bg='Black', fg='White', command=uptade2)
b3 = tk.Button(text='', height = 15, width = 39, bg='Black', fg='White', command=uptade3)
b4 = tk.Button(text='', height = 15, width = 39, bg='Black', fg='White', command=uptade4)
b5 = tk.Button(text='', height = 15, width = 39, bg='Black', fg='White', command=uptade5)
b6 = tk.Button(text='', height = 15, width = 39, bg='Black', fg='White', command=uptade6)
b7 = tk.Button(text='', height = 15, width = 39, bg='Black', fg='White', command=uptade7)
b8 = tk.Button(text='', height = 15, width = 39, bg='Black', fg='White', command=uptade8)
b9 = tk.Button(text='', height = 15, width = 39, bg='Black', fg='White', command=uptade9)
b1.grid(row=1, column=1)
b2.grid(row=1, column=2)
b3.grid(row=1, column=3)
b4.grid(row=2, column=1)
b5.grid(row=2, column=2)
b6.grid(row=2, column=3)
b7.grid(row=3, column=1)
b8.grid(row=3, column=2)
b9.grid(row=3, column=3)

window.mainloop()