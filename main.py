from tkinter import *
from pandas import *
from tkinter import messagebox
import random

# Constant

BACKGROUND_COLOR = "#B1DDC6"
word_data = []
words_to_learn = []

# CSV Data Reading

try:
    data = read_csv("data/words_to_learn.csv")
    words_data = data.to_dict("records")
except:
    data = read_csv("data/french_words.csv")
    words_data = data.to_dict("records")

# Function for words to learn

def learn_words():
    df = DataFrame(words_to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    messagebox.showinfo(title="Completed", message="You Have completed the flip card test. \nIf you weren't able to answer, restart it you will only get those words which you weren't able to get.")

# Random Word Selection

def random_word():
    word_data.clear()
    word_data.append(random.choice(words_data))

# Function to display words

def display_words():
    random_word()
    french = word_data[0]['French']
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=f"{french}")
    window.after(3000, flip_card)
    window.after_cancel(display_words)

# Function if right

def display_words_right():
    words_data.remove(word_data[0])
    canvas.itemconfig(bg_image, image=card_front_img)
    if len(words_data) == 0:
        learn_words()
    else:
        display_words()

# Function if wrong

def display_words_wrong():
    words_to_learn.append(word_data[0])
    words_data.remove(word_data[0])
    canvas.itemconfig(bg_image, image=card_front_img)
    if len(words_data) == 0:
        learn_words()
    else:
        display_words()

# Function to Flip the card

def flip_card():
    english = word_data[0]['English']
    canvas.itemconfig(bg_image, image=card_back_img)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=f"{english}")
    window.after_cancel(flip_card)

# UI Setup

window = Tk()
window.title("French Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
bg_image = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="Title",fill="black",font=("Ariel",40,"italic"))
word = canvas.create_text(400, 263, text="Word",fill="black",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=display_words_wrong)
wrong_button.grid(row=1, column=0)
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=display_words_right)
right_button.grid(row=1, column=1)
window.after(5000, display_words)

window.mainloop()