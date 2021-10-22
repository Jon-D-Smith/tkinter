from tkinter import *

root = Tk()

#Creating elements
myLabel1 = Label(root, text="Hello World!").grid(column=0,row=0)
myLabel2 = Label(root, text="My name is Jon Smith").grid(column=0,row=1)


root.mainloop()