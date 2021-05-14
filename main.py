from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#eec4c4"
RED = "#ffaaa7"
GREEN = "#98ddca"
BG = "#f7f3e9"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    countdown(300)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer, text=f'{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')
    if count > 0:
        window.after(1000, countdown, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=BG)

canvas = Canvas(width=200, height=224, bg=BG, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)
timer = canvas.create_text(100, 133, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

title = Label(text='Timer', font=(FONT_NAME, 50, 'normal'), bg=BG, fg=GREEN)
check = Label(text='✔︎', font=(FONT_NAME, 20, 'normal'), bg=BG, fg=GREEN)
title.grid(row=0, column=1)
check.grid(row=3, column=1)

start_btn = Button(text='Start', highlightthickness=0, command=start_timer)
reset_btn = Button(text='Reset', highlightthickness=0)
start_btn.grid(row=2, column=0)
reset_btn.grid(row=2, column=2)

window.mainloop()
