from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def button_clicked():
    in_km = round(float(user_input.get()) * 1.609, 2)
    answer_label.config(text=in_km)


user_input = Entry(width=10)
user_input.grid(row=0, column=1)

label_1 = Label(text="Miles")
label_1.grid(row=0, column=2)

label_2 = Label(text="is equals to")
label_2.grid(row=1, column=0)

answer_label = Label(text="0")
answer_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
