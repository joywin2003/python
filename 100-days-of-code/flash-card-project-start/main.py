from tkinter import *
import pandas
import time
import random

BACKGROUND_COLOR = "#B1DDC6"
HEADING = ("Ariel", 40, "italic")
WORD = ("Ariel", 60, "bold")

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
finally:
    to_learn = df.to_dict(orient="records")
    print(len(to_learn))
    current_card = {}


def right_answer():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index= False)
    next_word()


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(lan, text="French")
    canvas.itemconfig(words, text=current_card["French"])
    canvas.itemconfig(canvas_image, image=my_image_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(lan, text="English")
    canvas.itemconfig(words, text=current_card["English"])
    canvas.itemconfig(canvas_image, image=my_image_back)


# fill = "black"
# fill="white"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

pandas.read_csv("data/french_words.csv")
canvas = Canvas(width=800, height=526)
my_image_back = PhotoImage(file="images/card_back.png")
my_image_front = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=my_image_front)
lan = canvas.create_text(400, 150, text="", font=HEADING, fill="black")
words = canvas.create_text(400, 263, text="", font=WORD, fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

my_image1 = PhotoImage(file="images/right.png")
button = Button(image=my_image1, command=right_answer)
button.grid(row=1, column=0)

my_image2 = PhotoImage(file="images/wrong.png")
button = Button(image=my_image2, command=next_word)
button.grid(row=1, column=1)

next_word()

window.mainloop()
