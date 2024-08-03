from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("This is a Window")


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesnocancel, askyesno
def popup():
    response = messagebox.showinfo("Popup", "This is a popup")
    Label(root, text=response).pack()  # will return ok
    if response == "ok":
        Label(root, text="You clicked ok!").pack()


def warning():
    response = messagebox.showwarning("Warning", "This is a warning!")
    Label(root, text=response).pack()  # will return ok
    if response == "ok":
        Label(root, text="You clicked ok!").pack()


def error():
    response = messagebox.showerror("Error", "This is an error!")
    Label(root, text=response).pack()  # will return ok
    if response == "ok":
        Label(root, text="You clicked ok!").pack()


def question():
    response = messagebox.askquestion("Question", "This is a question")
    Label(root, text=response).pack()
    if response == "yes":
        Label(root, text="You clicked yes!").pack()
    else:
        Label(root, text="You clicked no!").pack()


def ok_cancel():
    response = messagebox.askokcancel("Ok or Cancel", "This is a ask or cancel message")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked ok!").pack()
    else:
        Label(root, text="You clicked cancel!").pack()


def yes_no_cancel():
    response = messagebox.askyesnocancel("Yes or No", " This is a message that asks yes or no")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked yes!").pack()
    elif response == 0:
        Label(root, text="You clicked no!").pack()
    else:
        Label(root, text="You clicked cancel!").pack()


Button(root, text="Click me for a popup that shows info!", command=popup).pack()
Button(root, text="Click me for a popup that shows a warning", command=warning).pack()
Button(root, text="Click me for a popup that shows an error", command=error).pack()
Button(root, text="Click me for a popup that shows a question", command=question).pack()
Button(root, text="Click me for a popup that shows a confirmation", command=ok_cancel).pack()
Button(root, text="Click me for a popup that shows a Yes or No", command=yes_no_cancel).pack()


mainloop()
