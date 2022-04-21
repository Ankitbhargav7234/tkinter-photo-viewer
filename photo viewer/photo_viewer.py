from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Image Viewer")
root.iconbitmap("foto.ico")

my_img1=ImageTk.PhotoImage(Image.open("images/shivji.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("images/lotus.png"))
my_img3=ImageTk.PhotoImage(Image.open("images/sunset.jpg"))
my_img4=ImageTk.PhotoImage(Image.open("images/white_sparkles.jpg"))
my_img5=ImageTk.PhotoImage(Image.open("images/headphones.jpg"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def back(num): 
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget() 

	my_label=Label(image=image_list[num])
	button_forward=Button(root,text=">>",command=lambda: forward(num+1))
	button_back=Button(root,text="<<",command=lambda: back(num-1))

	if num==0:
		button_back=Button(root,text="<<",state= DISABLED)

	my_label.grid(row=0,column=0,columnspan=3)
	button_forward.grid(row=1,column=2)
	button_back.grid(row=1,column=0)

def forward(num):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget() 

	my_label=Label(image=image_list[num])
	button_forward=Button(root,text=">>",command=lambda: forward(num+1))
	button_back=Button(root,text="<<",command=lambda: back(num-1))

	if num==len(image_list)-1:
		button_forward=Button(root,text=">>",state= DISABLED)

	my_label.grid(row=0,column=0,columnspan=3)
	button_forward.grid(row=1,column=2)
	button_back.grid(row=1,column=0)

button_back=Button(root,text="<<",command=back, state= DISABLED).grid(row=1,column=0)
button_quit=Button(root,text="Quit Program",command=root.quit).grid(row=1,column=1)
button_forward=Button(root,text=">>",command=lambda: forward(1)).grid(row=1,column=2)




root.mainloop()