from tkinter import *
from tkinter import ttk

root = Tk()

def printSecret():
    print("This is a secret")

count = 0
def addCount():
    global count
    countLabel["text"] = "adding..."
    return 
def subtractCount():
    global count
    count-=1
    return



frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0,row=0)
ttk.Button(frm, text='Quit', command=root.destroy).grid(column=1, row=1)
ttk.Button(frm, text='Secret', command=printSecret).grid(column=0, row=1)
ttk.Button(frm, text="-", command=subtractCount).grid(column=0, row=3)
ttk.Label(frm, text="0").grid(column=1, row=3)
ttk.Button(frm, text="+", command=addCount).grid(column=2, row=3)
root.mainloop()