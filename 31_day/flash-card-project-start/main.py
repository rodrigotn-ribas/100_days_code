import random
from dataclasses import field
from pydoc import text
from tkinter import *
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/hsk1.csv")
to_learn = data.to_dict(orient="records")
current_card = random.choice(to_learn)


# ------------------------- Button Function --------------------------- #
def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="Mandarim", fill="black")
    canvas.itemconfig(card_word, text=current_card["Mandarim"], fill="black")
    canvas.itemconfig(pinyin_word_label, text=current_card["Pinyin"], fill="black")
    window.after(5000, flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(pinyin_word_label, text="")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashly")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR) # Image size
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 120, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 250, text="word", font=("Arial", 60, "bold"))
pinyin_word_label = canvas.create_text(400, 390, text="pinyin", font=("Arial", 60, "bold"))

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)

next_card()
window.after(3000, flip_card)

window.mainloop()