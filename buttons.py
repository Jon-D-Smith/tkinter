from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look, I clicked a button!").pack()

myButton = Button(root, text="Click Me!", padx=50, command=myClick).pack()

root.mainloop()