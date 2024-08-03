from tkinter import *
from tkinter import ttk


def when_click():
    myLabel3 = Label(frame, text="Your age is " + myInput.get(), bd=10, relief=SUNKEN)
    myLabel3.grid(row=4, column=0)


#  Widget Hierarchy: all widgets are part of a widget hierarchy: parents and children
#  the root is the toplevel window.
root = Tk()
root.title("Just a Basic Program")

frame = LabelFrame(root, text="This is a frame", padx=100, pady=100)
frame.pack()

# creating labels
# grid system
# the downside of grids is that they are relative
# we could just treat grid as an object and append it by the end of the label
myLabel = Label(frame, text="Enter Your Age").grid(row=0,
                                                   column=0)  # You could append grid as an object but if you call
# the label, it will return None because in Python a().b() the result is what b() returns

# Input Fields
myInput = Entry(frame, width=50, borderwidth=4)
myInput.grid(row=2, column=0)

# creating a button
myButton = Button(frame, text="Would you like to click me?", padx=50, pady=10, fg="gray", bg="white",
                  command=when_click)
myButton.grid(row=3, column=0)

root = mainloop()
