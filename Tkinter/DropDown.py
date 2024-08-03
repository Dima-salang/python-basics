from tkinter import *

root = Tk()
root.title("Drop Down Menus")


def show():
    Selection = Label(root, text=clicked.get()).pack()


breakfast = ["Bacon", "Eggs", "Ham"]

clicked = StringVar()
clicked.set(breakfast[0])
down = OptionMenu(root, clicked, *breakfast).pack()

button = Button(root, text="Show selection", command=show).pack()

mainloop()