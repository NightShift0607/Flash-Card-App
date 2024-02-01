from tkinter import *
from pandas import *
import random

# Constant

BACKGROUND_COLOR = "#B1DDC6"

# CSV Data Reading

data = read_csv("data/french_words.csv")
words_data = data.to_dict("records")

# Random Word Selection

def random_word():
    rand_index = random.randint(0, 100)
    word_data = []
    word_data.append(words_data[rand_index])
    return word_data

# Function to display words

def display_words():
    word_data = random_word()
    french = word_data[0]['French']
    english = word_data[0]['English']
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=f"{french}")

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
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=display_words)
wrong_button.grid(row=1, column=0)
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=display_words)
right_button.grid(row=1, column=1)

window.mainloop()