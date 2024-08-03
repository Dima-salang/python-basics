from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.geometry("720x480")
root.title("A Simple Image Viewer")


def open_image_viewer():
    global image_display
    global image_number
    top = Toplevel()
    top.title("Image Viewer")
    image_list = []
    top.filename = filedialog.askopenfilenames(initialdir="/", title="Select Directory", filetypes=(
    ("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))
    for file in top.filename:
        im = Image.open(file)
        resized = im.resize((720, 400), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized)
        image_list.append(new_image)

    image_display = Label(top, image=image_list[0])
    image_display.grid(row=0, column=0, columnspan=3)

    def go_forward(image_number):
        global image_display
        global forward_button
        global back_button

        if image_number == 1 or 0:
            back_button = Button(top, text="<<", command=go_back, state=DISABLED)
            back_button.grid(row=1, column=0)

        if image_number+1 == len(image_list):
            forward_button = Button(top, text=">>", state=DISABLED)
            forward_button.grid(row=1, column=2)

        image_display.grid_forget()
        image_display = Label(top, image=image_list[image_number + 1])
        image_display.grid(row=0, column=0, columnspan=3)

        forward_button = Button(top, text=">>", command=lambda: go_forward(image_number + 1))
        back_button = Button(top, text="<<", command=lambda: go_back(image_number - 1))
        status = Label(top, text=f"Image {(image_number + 1) + 1} of {str(len(image_list))}")
        status.grid(row=2, column=1)
        back_button.grid(row=1, column=0)
        forward_button.grid(row=1, column=2)

    def go_back(image_number):
        global image_display
        global forward_button
        global back_button

        image_display.grid_forget()
        image_display = Label(top, image=image_list[image_number + 1])
        image_display.grid(row=0, column=0, columnspan=3)

        forward_button = Button(top, text=">>", command=lambda: go_forward(image_number + 1))
        back_button = Button(top, text="<<", command=lambda: go_back(image_number - 1))
        status = Label(top, text=f"Image {(image_number + 1) + 1} of {str(len(image_list))}")
        status.grid(row=2, column=1)
        back_button.grid(row=1, column=0)
        forward_button.grid(row=1, column=2)

        if image_number == 1 or 0:
            back_button = Button(top, text="<<", command=go_back, state=DISABLED)
            back_button.grid(row=1, column=0)

    # creating buttons
    forward_button = Button(top, text=">>", command=lambda: go_forward(0))
    back_button = Button(top, text="<<", command=go_back, state=DISABLED)
    exit_button = Button(top, text="Exit", command=top.quit)

    # create status bar
    status = Label(top, text=f"Image 1 of {len(image_list)}")

    # displaying buttons
    exit_button.grid(row=1, column=1, pady=10)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)

    # displaying status
    status.grid(row=2, column=1)

    if image_number == 1 or 0:
        back_button = Button(top, text="<<", command=go_back, state=DISABLED)
        back_button.grid(row=1, column=0)

    if image_number == len(image_list):
        forward_button = Button(top, text=">>", state=DISABLED)
        forward_button.grid(row=1, column=2)


Label(root, text="Welcome!").pack()
Button(root, text="Select directory", command=open_image_viewer).pack()

root.mainloop()
