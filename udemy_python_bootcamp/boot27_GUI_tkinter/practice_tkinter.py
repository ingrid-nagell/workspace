import tkinter
from tkinter.font import BOLD

from click import command

# create component
# define display opts

# window config
window = tkinter.Tk()
window.title("My GUI")
window.minsize(width=500, height=300)

# text label
label = tkinter.Label(text="This is a label", font=('Arial', 24, BOLD))
label.pack() # where to pack (put) label

# button
def button_click():
    new_label = input.get()
    label.config(text=new_label)

button = tkinter.Button(text="Click me", command=button_click)
button.pack()

# entry (input)
input = tkinter.Entry(width=10)
input.pack()

# keep the window open, always at the end
window.mainloop()

