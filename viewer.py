from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.title('Icons will be icons')
root.iconbitmap('panda.ico')

img1 = ImageTk.PhotoImage(Image.open('images/panda.png'))
img2 = ImageTk.PhotoImage(Image.open('images/Headshot.jpg'))
img3 = ImageTk.PhotoImage(Image.open('images/images.jpg'))

image_list = [img1, img2, img3]

my_label = Label(image=image_list[0])
my_label.grid(row=0,column=0, columnspan=3)

# buttons
button_back = Button(root, text="<<")
button_back.grid(row=1,column=0)
button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.grid(row=1, column=1)
button_forward = Button(root, text=">>")
button_forward.grid(row=1, column=2)

root.mainloop()