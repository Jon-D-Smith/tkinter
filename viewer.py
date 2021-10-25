from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.title('Icons will be icons')
root.iconbitmap('panda.ico')

img1 = ImageTk.PhotoImage(Image.open('images/panda.png'))
img2 = ImageTk.PhotoImage(Image.open('images/Headshot.jpg'))
img3 = ImageTk.PhotoImage(Image.open('images/images.jpg'))
my_label = Label(image=img1).pack()


button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()

root.mainloop()