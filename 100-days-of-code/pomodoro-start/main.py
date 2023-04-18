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
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg="GREEN")
    tick_label.config(text="")
    global reps
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# def count_down(second,minute):
#     if minute > 0:
#         canvas.itemconfig(timer_text, text=f"{minute}:{second}")
#         if second == 0:
#             minute -= 1
#             second = 60
#             window.after(100, count_down, second,minute)
#         if second>0:
#             window.after(100, count_down, second - 1,minute)

def count_down(count):
        minute = math.floor(count/60)
        second = count%60
        if second < 10:
            second = f"0{second}"
        canvas.itemconfig(timer_text, text=f"{minute}:{second}")
        if count>0:
            global timer
            timer = window.after(1, count_down, count - 1)
        else:
            start_timer()
            global reps
            if reps % 2 != 0:
                tick_label.config(text="✓")
            else:
                tick_label.config(text="")



def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="LONG BREAK", fg=PINK)
    elif reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="WORK TIME", fg=RED)
    elif reps % 2 == 0:
        count_down(break_sec)
        timer_label.config(text="BREAK TIME", fg=GREEN)
    reps += 1


def end_timer():
    count_down()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "normal"))
timer_label.grid(row=0, column=1)

tick_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "normal"))
tick_label.grid(row=3, column=1)


start_button = Button(text="Start", highlightthickness=0, bd=0, command=start_timer)
start_button.grid(row=2, column=0)

end_button = Button(text="End", highlightthickness=0, command=reset_timer)
end_button.grid(row=2, column=2)

canvas = Canvas(width=200, height=234, bg=YELLOW, highlightthickness=0, )
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(100, 134, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
window.mainloop()
