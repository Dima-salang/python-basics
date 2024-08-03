from tkinter import *

root = Tk()
root.title("Checkboxes")


def show():
    myLabel = Label(root, text=var.get()).pack()


var = IntVar()
my_box = Checkbutton(root, text="Check this box!", variable=var).pack()
my_button = Button(root, text="Show selection", command=show).pack()



mainloop()