from tkinter import *

root = Tk()
root.title("Forms")

frame1 = LabelFrame(root, padx=100, pady=100)
frame1.grid(row=0, column=0)

correct_answers = 0

test_questions = [
    "What is the nearest planet from the Sun?",
    "What is the largest country in the world?",
    "What is the widest ocean in the world?"
]

test_options = [
    (
        ("Mercury", "Mercury"),
        ("Mars", "Mars"),
        ("Earth", "Earth"),
        ("Jupiter", "Jupiter")
    ),
    (
        ("America", "America"),
        ("Russia", "Russia"),
        ("China", "China"),
        ("Philippines", "Philippines")
    ),
    (
        ("Pacific Ocean", "Pacific Ocean"),
        ("Atlantic Ocean", "Atlantic Ocean")
    )

]

answers = [
    "Mercury",
    "Russia",
    "Pacific Ocean"
]

test = StringVar()
test.set(None)

test_question = Label(frame1, text=test_questions[0])
test_question.pack()

for question, answer in test_options[0]:
    form_options = Radiobutton(frame1, text=question, variable=test, value=answer)
    form_options.pack()

# create buttons
submit = Button(frame1, text="Submit", command=lambda: clicked(test.get()))
submit.pack()

forward = Button(frame1, text="Next question", command=lambda: go_forward(0))
forward.pack()

backward = Button(frame1, text="Go back", command=lambda: go_backward(0))
backward.pack()


def clicked(value):
    global answers
    global correct_answers
    global submit
    if value in answers:
        submit.pack_forget()
        submit = Button(frame1, text="Submit", command=lambda: clicked(test.get()), state=DISABLED)
        submit.pack()
        show = Label(frame1, text="You got it right!")
        show.pack()
        correct_answers += 1
        counter = Label(frame1, text=f"You have answered {correct_answers} out of {len(test_questions)} correctly!")
        counter.pack()
    else:
        show = Label(frame1, text="Try again!")
        show.pack()


def go_forward(value):
    global test_question
    global form_options
    global frame1

    frame1.grid_forget()
    frame1 = LabelFrame(root, padx=100, pady=100)
    frame1.grid(row=0, column=0)

    test = StringVar()
    test.set(None)

    test_question = Label(frame1, text=test_questions[value + 1])
    test_question.pack()

    for question, answer in test_options[value + 1]:
        Radiobutton(frame1, text=question, variable=test, value=answer).pack()

    # create buttons
    submit = Button(frame1, text="Submit", command=lambda: clicked(test.get()))
    submit.pack()

    forward = Button(frame1, text="Next question", command=lambda: go_forward(value + 1))
    forward.pack()

    backward = Button(frame1, text="Go back", command=lambda: go_backward(value - 1))
    backward.pack()


def go_backward(value):
    global test_question
    global form_options
    global frame1

    frame1.grid_forget()
    frame1 = LabelFrame(root, padx=100, pady=100)
    frame1.grid(row=0, column=0)

    test = StringVar()
    test.set(None)

    test_question = Label(frame1, text=test_questions[value - 1])
    test_question.pack()

    for question, answer in test_options[value - 1]:
        Radiobutton(frame1, text=question, variable=test, value=answer).pack()

    # create buttons
    submit = Button(frame1, text="Submit", command=lambda: clicked(test.get()))
    submit.pack()

    forward = Button(frame1, text="Next question", command=lambda: go_forward(value + 1))
    forward.pack()
    backward = Button(frame1, text="Go back", command=lambda: go_backward(value - 1))
    backward.pack()


if correct_answers == len(test_questions):
    frame1.grid_forget()
    frame1 = LabelFrame(root, padx=100, pady=100)
    frame1.grid(row=0, column=0)
    message = Label(frame1, text="Congratulations! You have finished the form!")
    message.pack()
    exit_button = Button(frame1, text="Exit", command=root.quit())
    exit_button.pack()
mainloop()
