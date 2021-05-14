from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#eec4c4"
RED = "#f14668"
GREEN = "#98ddca"
BG = "#f7f3e9"
FONT_NAME = "Courier"
WORK_SEC = 25 * 60
SHORT_BREAK_SEC = 5 * 60
LONG_BREAK_SEC = 20 * 60
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1

    if REPS == 8:
        title.config(fg=RED, text='Break')
        countdown(LONG_BREAK_SEC)
        REPS = 0
    elif REPS % 2 == 0:
        title.config(fg=PINK, text='Break')
        countdown(SHORT_BREAK_SEC)
    else:
        title.config(fg=GREEN, text='Work')
        countdown(WORK_SEC)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer, text=f'{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')
    if count >= 0:
        global TIMER
        TIMER = window.after(1000, countdown, count - 1)
    else:
        check.config(text='✔︎'*(REPS // 2))
        start_timer()

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
check = Label(text='', font=(FONT_NAME, 30, 'normal'), bg=BG, fg=GREEN)
title.grid(row=0, column=1)
check.grid(row=3, column=1)

start_btn = Button(text='Start', highlightthickness=0, command=start_timer)
reset_btn = Button(text='Reset', highlightthickness=0)
start_btn.grid(row=2, column=0)
reset_btn.grid(row=2, column=2)

window.mainloop()
