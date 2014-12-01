#JI-69
from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=400,height=950, background='grey')
drawpad.grid(row=0, column=1)

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