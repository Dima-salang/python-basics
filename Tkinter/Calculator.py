from tkinter import *

root = Tk()
root.title("A Simple Calculator")

enter_num = Entry(root, width=40, borderwidth=4,)
enter_num.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = enter_num.get()
    enter_num.delete(0, END)
    enter_num.insert(0, str(current) + str(number))


def clear_click():
    enter_num.delete(0, END)


def num_add():
    global num1
    global math
    math = "addition"
    num1 = enter_num.get()
    enter_num.delete(0, END)


def num_subtract():
    global num1
    global math
    math = "subtraction"
    num1 = enter_num.get()
    enter_num.delete(0, END)


def num_multiply():
    global num1
    global math
    math = "multiplication"
    num1 = enter_num.get()
    enter_num.delete(0, END)


def num_divide():
    global num1
    global math
    math = "division"
    num1 = enter_num.get()
    enter_num.delete(0, END)


def equal_click():
    num2 = enter_num.get()
    enter_num.delete(0, END)
    if math == "addition":
        enter_num.insert(0, int(num1) + int(num2))
    elif math == "subtraction":
        enter_num.insert(0, int(num1) - int(num2))
    elif math == "multiplication":
        enter_num.insert(0, int(num1) * int(num2))
    else:
        enter_num.insert(0, int(num1) / int(num2))


# defining buttons
num_button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
num_button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
num_button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
num_button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
num_button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
num_button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
num_button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
num_button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
num_button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
num_button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

add_button = Button(root, text="+", padx=40, pady=20, command=lambda: num_add())
subtract_button = Button(root, text="-", padx=40, pady=20, command=lambda: num_subtract())
multiply_button = Button(root, text="x", padx=39, pady=20, command=lambda: num_multiply())
divide_button = Button(root, text="/", padx=41, pady=20, command=lambda: num_divide())
equal_button = Button(root, text="=", padx=88, pady=20, command=lambda: equal_click())
clear_button = Button(root, text="Clear", padx=79, pady=20, command=lambda: clear_click())

# displaying
subtract_button.grid(row=6, column=0)
multiply_button.grid(row=6, column=1)
divide_button.grid(row=6, column=2)
num_button0.grid(row=4, column=0)
add_button.grid(row=5, column=0)
equal_button.grid(row=4, column=1, columnspan=2)
clear_button.grid(row=5, column=1, columnspan=2)

num_button1.grid(row=3, column=0)
num_button2.grid(row=3, column=1)
num_button3.grid(row=3, column=2)

num_button4.grid(row=2, column=0)
num_button5.grid(row=2, column=1)
num_button6.grid(row=2, column=2)

num_button7.grid(row=1, column=0)
num_button8.grid(row=1, column=1)
num_button9.grid(row=1, column=2)


root = mainloop()