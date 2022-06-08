from tkinter import *
from unittest import result

from requests import delete

def enter_name():
    write_name = field1.get()
    # print(write_name)
    output["text"] = f"Labas  {write_name}"

def delete():
    result["text"] = ""



window = Tk()

menu = Menu(window)
window.config(menu=menu)
submenu = Menu(menu, tearoff = 0)
window.geometry("300x80")

menu.add_cascade(label="Meniu", menu=submenu)
submenu.add_command(label="Išvalyti", command=delete)
submenu.add_command(label="Atkurti", command=enter_name)
submenu.add_separator()
submenu.add_command(label="Išeiti",)

window.geometry("300x80")
name = Label(window, text="Name")
field1 = Entry(window)
button = Button(window, text="Enter", command=enter_name)
output = Label(window, text="")
window.bind("<Return>", lambda event: enter_name())
# button.pack()

name.grid(row=0, column=0, sticky=W)
field1.grid(row=0, column=1, sticky=W)
button.grid(row=0, column=2, sticky=W)
output.grid(row=1, column=1, sticky=W)

window.mainloop()