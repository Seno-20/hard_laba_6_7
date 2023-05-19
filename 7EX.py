from tkinter import *
import tkinter as tk

root = Tk()
root.title("NAME")
root.geometry("480x480+360+120")

price = IntVar() # создаем переменную, которую будем использовать для хранения значения цены

#функция, которая будет вызываться при выборе radiobutton

#функция, которая будет вызываться при нажатии на кнопку "ОК"
def calculate():
    result = int(entry.get()) * int(radio_var.get())
    output_label.config(text=str(result))

#создаем radiobuttonы и привязываем их к функции set_price
radio_var = tk.IntVar()
plastic_rb = Radiobutton(root, text="9x12", variable=radio_var, value="100").grid()
straw_rb = Radiobutton(root, text="10x15", variable=radio_var, value="200").grid()
aluminum_rb = Radiobutton(root, text="18x24", variable=radio_var, value="1000").grid()


#создаем поле ввода и кнопку "ОК"
entry = Entry(root)
entry.grid()
ok_button = Button(root, text="ОК", command=calculate)
ok_button.grid()

#создаем поле вывода для результата
output_label = Label(root, text="")
output_label.grid()

root.mainloop()