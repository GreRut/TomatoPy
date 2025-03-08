from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    countdown(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    canvas.itemconfig(timer, text=count)
    if count > 0:
        window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("TomatoTimer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
start = Button(text="Start", command=start_timer, highlightthickness=0)
reset = Button(text="Reset", highlightthickness=0)
tick = Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))

title_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)
tick.grid(column=1, row=3)

window.mainloop()
