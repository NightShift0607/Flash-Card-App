from tkinter import *
from pandas import *

# Constant

BACKGROUND_COLOR = "#B1DDC6"


# UI Setup

window = Tk()
window.title("French Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="Title",fill="black",font=("Ariel",40,"italic"))
word = canvas.create_text(400, 263, text="Word",fill="black",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()