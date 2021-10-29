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

def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))
	
	if image_number == 3:
		button_forward = Button(root, text=">>", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)
    
def back(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == 1:
		button_back = Button(root, text="<<", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

# buttons
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_back.grid(row=1,column=0)
button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.grid(row=1, column=1)
button_forward = Button(root, text=">>", command=lambda: forward(2))
button_forward.grid(row=1, column=2)

root.mainloop()