from tkinter import *


def calculate():
    miles = int(input.get())
    conv_factor = 1.609344
    km = miles * conv_factor
    blank_label.config(text=km)


window = Tk()
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)
window.title('Miles to KM')

# Creating labels for calculation
mile_label = Label(text='miles')
km_label = Label(text='km')
equal_label = Label(text='is equivalent to')
blank_label = Label(text='0')

# Creating button
calc_button = Button(text='Calculate', command=calculate)

# Creating Entry
input = Entry()

# Packing buttons and labels
mile_label.grid(row=0, column=2)
km_label.grid(row=1, column=2)
equal_label.grid(row=1, column=0)
blank_label.grid(row=1, column=1)
calc_button.grid(row=2, column=1)
input.grid(row=0, column=1)

window.mainloop()
