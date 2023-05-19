from tkinter import *  
from tkinter import Tk
from tkinter import ttk

def validate(new_value):                                                  # +++
    return new_value == "" or new_value.isnumeric()       
def on_select(event):
    selected_value = event.widget.get()
    if selected_value == "Пластик":
        price.set("1")
    elif selected_value == "Соломка":
        price.set("2")
    elif selected_value == "Алюминий":
        price.set("3")
    elif selected_value == "Текстиль":
        price.set("4")  
def calculation():
    
    label["text"] = int(txt_w.get())*int(txt_l.get()) *int(price.get())



window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('400x250')  
lbl = Label(window, text="Ширина (см.)")  
lbl.grid(column=0, row=0,pady=5, sticky=W)
lbl = Label(window, text="Длина (см.)")  
lbl.grid(column=0, row=1,pady=5, sticky=W)  
lbl = Label(window, text="Материал")  
lbl.grid(column=0, row=2,pady=5, sticky=W)

btn = Button(window, text="Ок", command=calculation, width=15)  
btn.grid(column=0, row=3, sticky=W,pady=10)  


vcmd = (window.register(validate), '%P')

txt_w = Entry(window,width=15, validate='key', validatecommand=vcmd)  
txt_w.grid(column=1, row=0)  

txt_l = Entry(window,width=15, validate='key', validatecommand=vcmd)  
txt_l.grid(column=1, row=1) 

first_parameter = ''
languages = ["Пластик", "Соломка", "Алюминий", "Текстиль"]
combobox =ttk.Combobox(state="readonly", values=languages, width=12)
combobox.bind("<<ComboboxSelected>>", on_select)
combobox.grid(column=1, row=2)

label = ttk.Label()
label.grid(column=0, row=4)     #площадь

price = StringVar()
price_label = Label(textvariable=price) #цена за кв.см.

window.mainloop()