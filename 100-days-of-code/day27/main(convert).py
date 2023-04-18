from tkinter import *

def converter():
    miles = int(entry.get())
    km = round(miles*1.609,2)
    label4 = Label(text=f"{km}")
    label4.grid(row=1, column=1)

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(10, 10)
window.config(padx=50,pady=50)

entry = Entry(width=10)
entry.grid(row=0, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="Km")
label3.grid(row=1, column=2)


button = Button(text="Calculate", command=converter)
button.grid(row=2,column=1)

window.mainloop()