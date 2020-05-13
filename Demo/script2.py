from tkinter import *

window = Tk()

def conversion():
    kg = float(e1_value.get())
    grams = kg * 1000
    pounds = kg * 2.204
    ounces = kg * 35.274

    t1.delete(1.0, END)
    t2.delete(1.0, END)
    t3.delete(1.0, END)

    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)


e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=0)

e2=Label(window,text="Kg")
e2.grid(row=0,column=1)

b1 = Button(window, text='Convert', command=conversion)
b1.grid(row=0, column=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=2)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=3)

window.mainloop()