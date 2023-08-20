from tkinter import *
from random import randint

root = Tk()
root.title("Thamarai's Password Generator")
root.geometry("600x400")

def new_rand():
    pw_entry.delete(0, END)
    pw_length = int(my_entry.get())
    my_password = ''

    for _ in range(pw_length):
        my_password += chr(randint(33, 126))
    pw_entry.insert(0, my_password)

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

def reset_fields():
    my_entry.delete(0, END)
    pw_entry.delete(0, END)
    username_entry.delete(0, END)

def accept_fields():
    username = username_entry.get()
    password = pw_entry.get()
    # You can do something with the username and password here, e.g., save to a file or a database.
    # For simplicity, we'll print them to the console.
    print("Username:", username)
    print("Password:", password)

lf = LabelFrame(root, text="Password Generator")
lf.pack(pady=20)

Label(lf, text="Username:").pack()
username_entry = Entry(lf, font=("Helvetica", 18))
username_entry.pack(pady=5, padx=20)

Label(lf, text="Password Length:").pack()
my_entry = Entry(lf, font=("Helvetica", 18))
my_entry.pack(pady=5, padx=20)

pw_entry = Entry(root, text='', font=("Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

reset_button = Button(my_frame, text="Reset Fields", command=reset_fields)
reset_button.grid(row=0, column=2, padx=10)

accept_button = Button(my_frame, text="Accept Fields", command=accept_fields)
accept_button.grid(row=0, column=3, padx=10)

root.mainloop()
