# Mile to km converter
from tkinter import *

def km_to_miles():
    miles = round(float(entry_miles.get()) * 1.609344, 2)
    text_output.config(text=miles)

window = Tk()
window.title("Mile to Km Converter")
#window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

entry_miles = Entry(width=10)
entry_miles.grid(column=1, row=0)

text_miles = Label(text="Miles")
text_miles.grid(column=2, row=0)

text_equal = Label(text="is equal to")
text_equal.grid(column=0, row=1)

text_output = Label(text=f"0")
text_output.grid(column=1, row=1)

text_km = Label(text="Km")
text_km.grid(column=2, row=1)

button_miles = Button(text="Calculate", command=km_to_miles)
button_miles.grid(column=1, row=2)

window.mainloop()
