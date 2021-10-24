from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.title('Icons will be icons')
root.iconbitmap('panda.ico')

my_img = ImageTk.PhotoImage(Image.open('panda.png'))
my_label = Label(image=my_img).pack()


button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()

root.mainloop()