from tkinter import *

def button_clicked():
    response = input.get()
    my_label.config(text=response)


window = Tk()
window.title("My first GUI")
window.minsize(10, 10)
window.config(padx=100,pady=20)

my_label = Label(text="I am alive")
my_label.grid(row=1,column=1)

input = Entry(width=10)
input.grid(row=2,column=2)




button = Button(text="click me", command=button_clicked)
button.grid(row=3,column=4)

new_button = Button(text="click m", command=button_clicked)
new_button.grid(row=1,column=3)


window.mainloop()
