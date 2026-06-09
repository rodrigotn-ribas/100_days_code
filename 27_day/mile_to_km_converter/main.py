from tkinter import *

# TODO: 4 labels, 1 button, 1 entry

#window
window = Tk()
window.title("Mile to Km Converter")

#function
def km_converter():
    km_converted["text"] = round(int(mile_input.get()) *  1.60934)

#Label
miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km_converted = Label(text="")
km_converted.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

#Button
button = Button(text="Calculate", command=km_converter)
button.grid(column=1, row=2)

#Entry
mile_input = Entry(width=7)
mile_input.insert(END, string="0")
mile_input.grid(column=1 , row=0)



window.mainloop()