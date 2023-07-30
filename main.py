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
reps = 0
timer = None
import math
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    check_mark.config(text='')
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN
    short_breake_sec = SHORT_BREAK_MIN
    long_breake_sec = LONG_BREAK_MIN

    if reps % 8 ==0:
        count_down(long_breake_sec)
        timer_label.config(text=f"{LONG_BREAK_MIN} min Breake", fg=RED)
    elif reps % 2 == 0:
        count_down(short_breake_sec)
        timer_label.config(text=f"{SHORT_BREAK_MIN} min Breake", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec <=9:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ''
        work_seasion = math.floor(reps/2)
        for _ in range(work_seasion):
            marks += "✔"
            check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg=YELLOW)

# def say_something(thing):
#     print(thing)
# window.after(1000, say_something, "hello")

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "italic"))
timer_label.grid(row=0, column=1)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(45))
check_mark.grid(row=3, column=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0, font=(FONT_NAME, 20))
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, font=(FONT_NAME, 20))
reset_button.grid(row=2,column=2)


canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)



window.mainloop()