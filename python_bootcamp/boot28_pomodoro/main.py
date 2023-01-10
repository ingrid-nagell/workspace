from tkinter import *
import math


img_path = "C:\\Users\\G020772\\workspace\\python_bootcamp\\boot28_pomodoro\\tomato.png"

# Constants
BGCOLOR = '#EAE0DA'
BUTTON_COLOR = '#F7F5EB'
FONT_NAME = 'Courier'

WORK_TIME = 25
SHORT_BREAK_TIME = 5
LONG_BREAK_TIME = 20

timer = None
reps = 0
marks = ""

# Timer reset
def reset_timer():
    global reps, marks
    window.after_cancel(timer)
    reps = 0
    marks = ""
    title.config(text="Timer", fg="green")
    timer_img.config(text="25:00")
    checkmarks.config(text="Sessions completed:")

# Timer mechanism
def start_timer():
    global reps, marks
    reps += 1
    work_sec = WORK_TIME * 60
    short_break_sec = SHORT_BREAK_TIME * 60
    long_break_sec = LONG_BREAK_TIME * 60
    if reps % 8 == 0:
        marks += "✔ "
        checkmarks.config(text=f"Sessions completed:\n{marks}")
        title.config(text="20 min break", fg='red')
        count_down(long_break_sec)
    elif reps % 2 == 0:
        marks += "✔ "
        checkmarks.config(text=f"Sessions completed:\n{marks}")
        title.config(text="5 min break", fg='red')
        count_down(short_break_sec)
    else:
        title.config(text="Time to focus", fg='green')
        count_down(work_sec)

# Count down mechanism
def count_down(seconds):
    global timer
    left_minutes = math.floor(seconds / 60)
    if left_minutes < 10:
        left_minutes = f"0{left_minutes}"
    left_seconds = seconds % 60
    if left_seconds < 10:
        left_seconds =  f"0{left_seconds}"

    timer_img.config(text=f"{left_minutes}:{left_seconds}")
    
    if seconds > 0:
        timer = window.after(1000, count_down, seconds-1)
    else:
        start_timer()

# User interface set up
window = Tk()
window.title("Pomodoro")
window.geometry('420x500')
window.config(padx=50, pady=50, bg=BGCOLOR)

bgimg = PhotoImage(file=img_path)
# Could use Canvas() instead
timer_img = Label(window, text="25:00", i=bgimg, bg=BGCOLOR, fg='white', font=(FONT_NAME, 20, 'bold'), compound='center')
timer_img.grid(column=1, row=1, padx=20, pady=20)

title = Label(text="Timer", font=(FONT_NAME, 24), bg=BGCOLOR, fg='green')
title.grid(column=1, row=0)

#title.config(text="Work")
#title.config(text="Break")

button_start = Button(text="Start", bg=BUTTON_COLOR, command=start_timer)
button_start.grid(column=0, row=2)
button_reset = Button(text="Reset", bg=BUTTON_COLOR, command=reset_timer)
button_reset.grid(column=2, row=2)

checkmarks = Label(text="Sessions completed:", fg="green", bg=BGCOLOR)
checkmarks.grid(column=1, row=3)


window.mainloop()
