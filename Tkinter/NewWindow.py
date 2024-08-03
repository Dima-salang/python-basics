from tkinter import *

root = Tk()
root.title("Original Window")


def open_window():
    top = Toplevel()
    top.title("New Window")
    Label(top, text="A label within the new window...").pack()


Button(root, text="Click me for a new window!", command=open_window).pack()

mainloop()