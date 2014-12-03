#JI-69
from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=400,height=725, background='grey')
drawpad.grid(row=0, column=1)

screen = drawpad.create_rectangle(50,50,350,250, fill = "white")
#Buttons 1-9
button0 = drawpad.create_rectangle(112.5,650,162.5,675, fill="white")
button1 = drawpad.create_rectangle(112.5,612.5,162.5,637.5, fill="white")
button2 = drawpad.create_rectangle(175,612.5,225,637.5, fill="white")
button3 = drawpad.create_rectangle(237.5,612.5,287.5,637.5, fill="white")
button4 = drawpad.create_rectangle(112.5,575,162.5,600, fill="white")
button2 = drawpad.create_rectangle(175,612.5,225,637.5, fill="white")
button2 = drawpad.create_rectangle(175,612.5,225,637.5, fill="white")
button2 = drawpad.create_rectangle(175,612.5,225,637.5, fill="white")


class MyApp:
    	def __init__(self, parent):
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="1", background= "white")
		self.button1.grid(row=0,column=0)
		
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="2", background= "white")
		self.button2.grid(row=0,column=1)
	

		
										


		drawpad.pack()
		
myapp = MyApp(root)


root.mainloop()