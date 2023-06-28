from tkinter import *
import math
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
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    title_lable.config (text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
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
    timer_countdown(work_sec)
    if reps % 8 == 0:
        timer_countdown(long_break_sec)
        title_lable.config(text="Break", fg=RED)
    elif reps % 2 ==0:
        timer_countdown(short_break_sec)
        title_lable.config(text="Break", fg=PINK)
    else:
        timer_countdown(work_sec)
        title_lable.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer_countdown(time):

    time_min = math.floor(time/60)
    time_sec = time % 60
    if time_sec<10:
        time_sec = f"0{time_sec}"
    canvas.itemconfig(timer_text, text = f"{time_min}:{time_sec}")
    if time>0:
        global timer
        timer = window.after(1000, timer_countdown, time -1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔️"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

window.after(1000, )

title_lable = Label(text="Timer",  fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_lable.grid(column=1,row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(102,112, image=img)
timer_text = canvas.create_text(102,112, text="00:00",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)



start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()