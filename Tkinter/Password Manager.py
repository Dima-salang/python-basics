from tkinter import *
import sqlite3

root = Tk()
root.title("Password Manager")

options_frame = Frame(root, height=100, width=250)
options_frame.grid(row=0, column=2, rowspan=4, columnspan=2)

display_frame = Frame(root, height=100, width=250)
display_frame.grid(row=0, column=0)

conn = sqlite3.connect("PassManager.db")

Cursor = conn.cursor()

# Create table
#Cursor.execute("""CREATE TABLE Passwords (
        #purpose text,
        #username text,
        #password text
#)""")


def insert_account():
    global display_frame
    conn = sqlite3.connect("PassManager.db")
    Cursor = conn.cursor()

    Cursor.execute("INSERT INTO Passwords VALUES (:purpose,:username,:password)",
                   {
                       'purpose': purpose.get(),
                       'username': username.get(),
                       'password': password.get()
                   }
                   )

    purpose.delete(0, END)
    username.delete(0, END)
    password.delete(0, END)

    conn.commit()
    conn.close()


def show_accounts():
    global display_frame
    display_frame.grid_forget()
    display_frame = LabelFrame(root, height=100, width=250)
    display_frame.grid(row=0, column=0)

    conn = sqlite3.connect("PassManager.db")
    Cursor = conn.cursor()

    Cursor.execute("SELECT *, oid FROM Passwords")
    accounts = Cursor.fetchall()
    print_accounts = ''
    for account in accounts:
        print_accounts += f" RowID: {account[3]} \n Account: {account[0]} \n Username: {account[1]} \n Password: {account[2]}  \n\n"

    query = Label(display_frame, text=print_accounts)
    query.grid(row=5, column=0, columnspan=2)

    conn.commit()
    conn.close()


def add_accounts():
    global display_frame
    global purpose
    global username
    global password
    display_frame.grid_forget()
    display_frame = Frame(root, height=100, width=250)
    display_frame.grid(row=0, column=0)

    purpose = Entry(display_frame, width=30)
    purpose_label = Label(display_frame, text="Account for:")
    username = Entry(display_frame, width=30)
    user_label = Label(display_frame, text="Enter your Username")
    password = Entry(display_frame, width=30)
    password_label = Label(display_frame, text="Enter your Password")
    submit = Button(display_frame, text="Submit", command=insert_account)

    purpose.grid(row=0, column=1)
    purpose_label.grid(row=0, column=0)
    username.grid(row=1, column=1)
    user_label.grid(row=1, column=0)
    password.grid(row=2, column=1)
    password_label.grid(row=2, column=0)
    submit.grid(row=3, column=0, columnspan=2)


def update_account():
    conn = sqlite3.connect("PassManager.db")
    Cursor = conn.cursor()

    Cursor.execute(f"""UPDATE Passwords SET
        purpose = :account,
        username = :user_name,
        password = :pass_word
        WHERE oid = :oid""",
                   {
                       'account': updated_purpose.get(),
                       'user_name': updated_username.get(),
                       'pass_word': updated_password.get(),
                       'oid': rowId.get()
                   }
                   )

    updated_purpose.delete(0, END)
    updated_username.delete(0, END)
    updated_password.delete(0, END)

    conn.commit()
    conn.close()


def edit_accounts():
    global display_frame
    global rowId
    display_frame.grid_forget()
    display_frame = Frame(root, height=100, width=250)
    display_frame.grid(row=0, column=0)

    def open_edit():
        global display_frame
        global updated_purpose
        global updated_username
        global updated_password

        display_frame.grid_forget()
        display_frame = Frame(root, height=100, width=250)
        display_frame.grid(row=0, column=0)

        updated_purpose = Entry(display_frame, width=30)
        purpose_label = Label(display_frame, text="Account for:")
        updated_username = Entry(display_frame, width=30)
        user_label = Label(display_frame, text="Enter your Username")
        updated_password = Entry(display_frame, width=30)
        password_label = Label(display_frame, text="Enter your Password")
        submit = Button(display_frame, text="Update", command=update_account)

        updated_purpose.grid(row=1, column=1)
        purpose_label.grid(row=1, column=0)
        updated_username.grid(row=2, column=1)
        user_label.grid(row=2, column=0)
        updated_password.grid(row=3, column=1)
        password_label.grid(row=3, column=0)
        submit.grid(row=4, column=0, columnspan=2)

        conn = sqlite3.connect("PassManager.db")
        Cursor = conn.cursor()

        Cursor.execute(f"SELECT * FROM Passwords WHERE oid = {rowId.get()}")
        accounts = Cursor.fetchall()
        for account in accounts:
            updated_purpose.insert(0, account[0])
            updated_username.insert(0, account[1])
            updated_password.insert(0, account[2])

        conn.commit()
        conn.close()



    rowId = Entry(display_frame, width=30)
    rowId_label = Label(display_frame, text="Enter RowID:")
    submit = Button(display_frame, text="Submit", command=open_edit)

    rowId.grid(row=0, column=1)
    rowId_label.grid(row=0, column=0)
    submit.grid(row=1, column=0, columnspan=2)


def delete_accounts():
    global display_frame
    global rowId
    display_frame.grid_forget()
    display_frame = Frame(root, height=100, width=250)
    display_frame.grid(row=0, column=0)

    def delete_account():
        conn = sqlite3.connect("PassManager.db")
        Cursor = conn.cursor()

        Cursor.execute(f"DELETE from Passwords WHERE oid = {rowId.get()}")
        rowId.delete(0, END)

        conn.commit()
        conn.close()

    rowId = Entry(display_frame, width=30)
    rowId_label = Label(display_frame, text="Enter RowID:")
    submit = Button(display_frame, text="Delete", command=delete_account)

    rowId.grid(row=0, column=1)
    rowId_label.grid(row=0, column=0)
    submit.grid(row=1, column=0, columnspan=2)



# Defining Widgets
purpose = Entry(display_frame, width=30)
purpose_label = Label(display_frame, text="Account for:")
username = Entry(display_frame, width=30)
user_label = Label(display_frame, text="Enter your Username")
password = Entry(display_frame, width=30)
password_label = Label(display_frame, text="Enter your Password")
submit = Button(display_frame, text="Submit", command=insert_account)
add_accounts = Button(options_frame, text="Add Account", command=add_accounts)
show = Button(options_frame, text="Show Accounts", command=show_accounts)
update_accounts = Button(options_frame, text="Update Accounts", command=edit_accounts)
delete_accounts = Button(options_frame, text="Delete Accounts", command=delete_accounts)

# Displaying widgets
purpose.grid(row=0, column=1)
purpose_label.grid(row=0, column=0)
username.grid(row=1, column=1)
user_label.grid(row=1, column=0)
password.grid(row=2, column=1)
password_label.grid(row=2, column=0)
submit.grid(row=3, column=0, columnspan=2)
show.grid(row=0, column=0, columnspan=2)
add_accounts.grid(row=1, column=0)
update_accounts.grid(row=2, column=0)
delete_accounts.grid(row=3, column=0)


conn.commit()

conn.close()

mainloop()