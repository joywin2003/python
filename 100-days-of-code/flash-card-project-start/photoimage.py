from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
HEADING = ("arial", 40, "italic")
WORD = ("arial", 60, "bold")


class PhotoImage:
    def __init__(self):
        self.fn_language = "french"
        self.en_language = "english"
        self.right_mark()
        self.wrong_mark()

    def front_image(self):
        canvas_front = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
        my_image_front = PhotoImage(file="images/card_front.png")
        button = Button(image=my_image_front, highlightthickness=0)
        french_text = canvas_front.create_text(400, 150, text=self.fn_language, font=HEADING)
        button.grid(row=0, column=0, columnspan=2)
    def back_image(self):
        canvas_back = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
        my_image_back = PhotoImage(file="images/card_back.png")
        button = Button(image=my_image_back, highlightthickness=0)
        french_text = canvas_back.create_text(400, 150, text=self.en_language, font=HEADING)
        button.grid(row=0, column=0, columnspan=2)

    def right_mark(self):
        my_image1 = PhotoImage(file="images/right.png")
        button = Button(image=my_image1, highlightthickness=0)
        button.grid(row=1, column=0)

    def wrong_mark(self):
        my_image2 = PhotoImage(file="images/wrong.png")
        button = Button(image=my_image2, highlightthickness=0)
        button.grid(row=1, column=1)
