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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

title_lable = Label(text="Timer",  fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_lable.grid(column=1,row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(102,112, image=img)
canvas.create_text(102,112, text="00:00",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

start_btn = Button(text="Start", highlightthickness=0)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0)
reset_btn.grid(column=2, row=2)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()