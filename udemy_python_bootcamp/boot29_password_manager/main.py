import tkinter as tk
import random as rd
import string
import pyperclip
from tkinter import messagebox

logo_path = "C:\\Users\\G020772\\workspace\\python_bootcamp\\boot29_password_manager\\logo.png"

# Constants
BG_COLOR = '#EFF5F5'
RED = '#EB6440'
DARK = '#497174'
LIGHT = '#D6E4E5'

# ----------- Functionality ------------ #
# Generate pws
def password_generator():
    letter_upper = string.ascii_uppercase
    letter_lower = string.ascii_lowercase
    digits_special_char = string.digits + "_-$?!%#£&"

    total_upper = rd.randint(1, 9)
    total_lower = (10 - total_upper)
    characters = rd.choices(letter_upper, k=total_upper) + rd.choices(letter_lower, k=total_lower) + rd.choices(digits_special_char, k=4)
    rd.shuffle(characters)
    password = ''.join(characters)
    
    pws_input.insert(0, string=password)
    pyperclip.copy(password) # Add to clipboard

# Update pws-file
def add():
    website = website_input.get()
    user = email_input.get()
    pws = pws_input.get()

    if website != "" and user != "" and pws != "":
        if messagebox.askokcancel("Password Manager", "Do you want to add this password?"):
            with open("passwords.txt", 'a') as f:
                f.write(f"{website}, {user}, {pws}\n")
            pws_input.delete(0, 'end')
            website_input.delete(0, 'end')
            website_input.focus()
    else:
        is_missing = ""
        if website == "":
            if is_missing == "":
                is_missing += "website"
            else: 
                is_missing += ", website"
        if user == "":
            if is_missing == "":
                is_missing += "username"
            else:
                is_missing += ", username"
        if pws == "":
            if is_missing == "":
                is_missing += "password"
            else:
                is_missing += ", password"
        messagebox.showinfo("Password Manager", f"Missing {is_missing}")


# ----------- User interface ----------- #
root = tk.Tk()
root.title("Password Manager")
# root.geometry('300x300')
root.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
logo = tk.PhotoImage(file=logo_path)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=1, column=2)

website_label = tk.Label(text="Website:")
website_label.grid(row=2, column=1)

website_input = tk.Entry()
website_input.grid(row=2, column=2, columnspan=2, sticky='WE', padx=10)
website_input.focus()

email_label = tk.Label(text="Email/Username:")
email_label.grid(row=3, column=1)

email_input = tk.Entry()
email_input.grid(row=3, column=2, sticky='EW', padx=10)
email_input.insert(0, string="ingrid@gmail.com")

pws_label = tk.Label(text="Password:")
pws_label.grid(row=4, column=1)

pws_input = tk.Entry()
pws_input.grid(row=4, column=2, sticky='EW', padx=10)

gen_pws_button = tk.Button(text="Generate Password", command=password_generator)
gen_pws_button.grid(row=4, column=3, sticky='EW', padx=10)

add_button = tk.Button(text="Add", command=add)
add_button.grid(row=5, column=2, columnspan=2, sticky='EW', padx=10)

status_label = tk.Label(text="")
status_label.grid(row=6, column=2, columnspan=2, sticky='EW', padx=10,  pady=10)

root.mainloop()