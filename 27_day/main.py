from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, ))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()

#Button
button = Button(text= "Click Me", command=button_clicked)
button.grid(column=1, row=1)

#Button 2
button2 = Button(text="New Button")
button2.grid(column=2, row=0)

#Entry
input = Entry(width= 10)
input.grid(column=3 , row=2)

window.mainloop()