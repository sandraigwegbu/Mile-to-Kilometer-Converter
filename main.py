from tkinter import *

FONT = ("Arial", 14, "normal")


def convert_to_km():
	miles = float(miles_input.get())
	km = round(miles * 1.609, 2)
	km_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=375, height=170)
window.config(padx=40, pady=30)

# Entry
miles_input = Entry(width=12, font=FONT)
miles_input.insert(END, "0")
miles_input.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0", font=FONT)
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

# Button
calculate_button = Button(text="Calculate", command=convert_to_km, font=FONT)
calculate_button.grid(column=1, row=2)

window.mainloop()
