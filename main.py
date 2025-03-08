from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_display, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_display, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("TomatoTimer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_display = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
start = Button(text="Start", command=start_timer, highlightthickness=0)
reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
check_marks = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))

title_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)
check_marks.grid(column=1, row=3)

window.mainloop()
