from pydoc import text
import tkinter as tk
from PIL import ImageTk, Image
import pandas as pd
from random import choice
from tkinter import messagebox

path_data = 'C:\\Users\\G020772\\workspace\\python_bootcamp\\boot31_flashcards\\french_words.csv'
all_data = pd.read_csv(path_data).to_dict(orient='records')
data = all_data[0:5]

path_front_image = 'C:\\Users\\G020772\\workspace\\python_bootcamp\\boot31_flashcards\\card_front.png'
path_back_image = 'C:\\Users\\G020772\\workspace\\python_bootcamp\\boot31_flashcards\\card_back.png'
path_wrong_button = 'C:\\Users\\G020772\\workspace\\python_bootcamp\\boot31_flashcards\\wrong.png'
path_right_button = 'C:\\Users\\G020772\\workspace\\python_bootcamp\\boot31_flashcards\\right.png'

bg_color= '#B1DDC6'
back_card_color = '#91c2af'
front_card_color = 'white'

elem = {}

###########################

def on_button_click(button_id):
    global elem, flip_timer, data, all_data
    if len(data) > 1:
        root.after_cancel(flip_timer)
        if button_id == 'right' and len(elem) > 0 :
            data.remove(elem)
        else:
            pass
        elem = choice(data)
        canvas.itemconfig(canvas_image, image=img_card_front)
        word_to_learn.config(text=elem['French'], bg=front_card_color, fg='black')
        language_title.config(text="French", bg=front_card_color, fg='black')
        flip_timer = root.after(3000, flip_card)
    else:
        data = all_data[0:5]
        messagebox.showinfo(title="Flashy", message=f"You know all the words!")
        on_button_click(0)
    word_counter.config(text=f"Words left to practice: {len(data)}")


def flip_card():
    canvas.itemconfig(canvas_image, image=img_card_back)
    language_title.config(text="English", bg=back_card_color, fg=front_card_color)
    word_to_learn.config(text=elem['English'], bg=back_card_color, fg=front_card_color)

###########################
# UI
root = tk.Tk()
root.title("Flashy")
root.config(padx=50, pady=50, bg=bg_color)

flip_timer = root.after(3000, flip_card)

word_counter = tk.Label(text=f"Words left to practice: {len(data)}", font=("Ariel", 20), bg=bg_color)
word_counter.grid(row=0, column=1, columnspan=2)

img_card_front = tk.PhotoImage(file=path_front_image)
img_card_back = tk.PhotoImage(file=path_back_image)

img_w_init = Image.open(path_wrong_button)
img_w_resized = img_w_init.resize((70,70), Image.ANTIALIAS)
img_wrong = ImageTk.PhotoImage(img_w_resized)

img_r_init = Image.open(path_right_button)
img_r_resized = img_r_init.resize((70,70), Image.ANTIALIAS)
img_right = ImageTk.PhotoImage(img_r_resized)

canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=bg_color)
canvas_image = canvas.create_image(410, 263, image=img_card_front)
canvas.grid(row=1, column=1, columnspan=2, pady=20)

language_title = tk.Label(canvas, text="French", font=("Ariel", 40, 'italic'), bg=front_card_color)
language_title.place(relx=0.5, rely=0.3, anchor='center')

word_to_learn = tk.Label(canvas, text="", font=("Ariel", 60, 'bold'), bg=front_card_color)
word_to_learn.place(relx=0.5, rely=0.5, anchor='center')

right_button = tk.Button(image=img_right, highlightthickness=0, command=lambda: on_button_click('right'))
right_button.grid(row=2, column=1)

wrong_button = tk.Button(image=img_wrong, highlightthickness=0, command=lambda: on_button_click('wrong'))
wrong_button.grid(row=2, column=2)

on_button_click(0)

root.mainloop()