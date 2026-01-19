import tkinter as tk
from tkinter import PhotoImage

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
def start_onClick():
    pass

def reset_onClick():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

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
canvas.create_text(104, 137, text="00:00",fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# label
timer_label = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45, "bold"))
timer_label.grid(column=1, row=0)

checkmark_label =tk.Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 17, "normal"))
checkmark_label.grid(column=1, row=3)

# botton
start_btn = tk.Button(text="Start",
                      font=(FONT_NAME, 12, "bold"),
                      fg=GREEN,
                      width=8,
                      height=1,
                      bg="white",
                      highlightthickness=0,
                      command=start_onClick)
start_btn.grid(column=0, row=2)
reset_btn = tk.Button(text="Reset",
                      font=(FONT_NAME, 12, "bold"),
                      fg=PINK,
                      width=8,
                      height=1,
                      bg="white",
                      highlightthickness=0,
                      command=reset_onClick)
reset_btn.grid(column=2, row=2)

window.mainloop()