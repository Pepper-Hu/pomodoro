import tkinter as tk
from tkinter import PhotoImage
import time
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
SEC_PER_MIN = 1
num_of_sessions = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_on_click():
    # stop count down
    window.after_cancel(timer)

    # reset session
    global num_of_sessions
    num_of_sessions = 0

    # reset UI
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_txt, text="00:00")
    checkmark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_on_click():
    global num_of_sessions
    num_of_sessions += 1
    print(num_of_sessions)

    work_starting_time = WORK_MIN * SEC_PER_MIN
    short_break_starting_time = SHORT_BREAK_MIN * SEC_PER_MIN
    ling_break_starting_time = LONG_BREAK_MIN * SEC_PER_MIN

    # session 1, 3, 5, 7
    if num_of_sessions % 2 == 1 and num_of_sessions < 8:
        count_down(work_starting_time)
        timer_label.config(text="Work", fg=GREEN)
    # session 2, 4, 6
    elif num_of_sessions % 2 == 0 and num_of_sessions < 8:
        count_down(short_break_starting_time)
        timer_label.config(text="Break", fg=PINK)
    # session 8
    elif num_of_sessions == 8:
        count_down(ling_break_starting_time)
        timer_label.config(text="Break", fg=RED)
    else:
        timer_label.config(text="Done!", fg=GREEN)
        return

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def format_time(count_num):
    count_min = math.floor(count_num / 60)
    count_sec = math.floor(count_num % 60)
    # : - Start of format specification
    # 0 - Fill character (what to pad with)
    # 2 - Minimum width (total characters)
    # d - Type specifier (decimal integer)
    return f"{count_min:02d}:{count_sec:02d}"

def count_down(count):
    # print(count)

    # # timer display using time
    # canvas.itemconfig(timer_txt, text=time.strftime('%M:%S', time.gmtime(count)))
    canvas.itemconfig(timer_txt, text=format_time(count))

    # When count down is on
    if count > 0:
        global timer
        # count every 1 second
        timer = window.after(1000, count_down, count -1)

    # when count down ends:
    else:
        # window popup on top of all other windows
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)

        # ring the bell
        window.bell()

        # start timer again
        start_on_click()

        # display checkmark when work session finished
        check_marks = ""
        work_sessions = math.floor(num_of_sessions / 2)

        for _ in range(work_sessions):
            check_marks += "✔"

        checkmark_label.config(text = check_marks)

# ---------------------------- UI SETUP ------------------------------- #
# window
window = tk.Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=70, bg=YELLOW)

# canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# tomato pic
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# time display
timer_txt = canvas.create_text(104, 137, text="00:00",fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# count_down(starting_time)

# label
timer_label = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45, "bold"))
timer_label.grid(column=1, row=0)

checkmark_label =tk.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 17, "normal"))
checkmark_label.grid(column=1, row=3)

# botton
start_btn = tk.Button(text="Start",
                      font=(FONT_NAME, 12, "bold"),
                      fg=GREEN,
                      width=8,
                      height=1,
                      bg="white",
                      highlightthickness=0,
                      command=start_on_click)
start_btn.grid(column=0, row=2)
reset_btn = tk.Button(text="Reset",
                      font=(FONT_NAME, 12, "bold"),
                      fg=PINK,
                      width=8,
                      height=1,
                      bg="white",
                      highlightthickness=0,
                      command=reset_on_click)
reset_btn.grid(column=2, row=2)

window.mainloop()