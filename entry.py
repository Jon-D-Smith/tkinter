from tkinter import *

root = Tk()
e = Entry(root, width=50)
e.pack()

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

Mybutton = Button(root, text="Submit your name", command=myClick).pack()

root.mainloop()