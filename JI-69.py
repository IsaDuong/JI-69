# -*- coding: utf-8 -*-
#JI-69
from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=400,height=725, background="grey")
drawpad.grid(row=0, column=1)

screen = drawpad.create_rectangle(50,50,350,250, fill = "white")
#Buttons 1-9
button0 = drawpad.create_rectangle(112.5,650,162.5,675, fill = "white")
button1 = drawpad.create_rectangle(112.5,612.5,162.5,637.5, fill = "white")
button2 = drawpad.create_rectangle(175,612.5,225,637.5, fill = "white")
button3 = drawpad.create_rectangle(237.5,612.5,287.5,637.5, fill = "white")
button4 = drawpad.create_rectangle(112.5,575,162.5,600, fill = "white")
button5 = drawpad.create_rectangle(175,575,225,600, fill = "white")
button6 = drawpad.create_rectangle(237.5,575,287.5,600, fill = "white")
button7 = drawpad.create_rectangle(112.5,537.5,162.5,562.5, fill = "white")
button8 = drawpad.create_rectangle(175,537.5,225,562.5, fill = 'white')
button9 = drawpad.create_rectangle(237.5,537.5,287.5,562.5, fill= 'white')
#Rest of Buttons
buttonENTER = drawpad.create_rectangle(237.5,650,350,675, fill='white')
buttonplus = drawpad.create_rectangle(300,612.5,350,637.5, fill='white')
buttonminus = drawpad.create_rectangle(300,575,350,600, fill='white')
buttonmultiply = drawpad.create_rectangle(300,537.5,350,562.5, fill='white')
buttondivide = drawpad.create_rectangle(300,500,350,525, fill='white')
buttonexponent = drawpad.create_rectangle(300,462.5,350,487.5, fill='white')
buttonbigarrow = drawpad.create_rectangle(300,425,350,450, fill='white')

buttonparenthesis = drawpad.create_rectangle(237.5,500,287.5,525, fill='white')
buttonTAN = drawpad.create_rectangle(237.5,462.5,287.5,487.5, fill='white')
buttoni = drawpad.create_rectangle(237.5,425,287.5,450, fill='white')

buttondot = drawpad.create_rectangle(175,650,225,675, fill='white')
buttonE = drawpad.create_rectangle(175,500,225,525, fill='white')
buttonCOS = drawpad.create_rectangle(175,462.5,225,487.5, fill='white')
button1dividedbyx = drawpad.create_rectangle(175,425,225,450, fill='white')
buttonRCL = drawpad.create_rectangle(175,387.5,225,412.5, fill='white')
buttonGTO = drawpad.create_rectangle(175,350,225,375, fill='white')

buttonsigmaplus = drawpad.create_rectangle(112.5,500,162,525, fill='white')
buttonSIN = drawpad.create_rectangle(112.5,462.5,162.5,487.5, fill='white')
buttonyexponentx = drawpad.create_rectangle(112.5,425,162.5,450, fill='white')
buttonxleftarrowrightarrowy = drawpad.create_rectangle(112.5,387.5,162.5,412.5, fill='white')
buttonMODE = drawpad.create_rectangle(112.5,350,162.5,375, fill='white')

buttonsigman = drawpad.create_rectangle(50,650,100,675, fill = 'white')
buttonCLEAR = drawpad.create_rectangle(50,612.5,100,637.5, fill = 'white')
buttonrightarrow = drawpad.create_rectangle(50,575,100,600, fill = '#3300FF')
buttonleftarrow = drawpad.create_rectangle(50,537.5,100,562.5, fill = '#EDDF1A')
buttonSERIES = drawpad.create_rectangle(50,500,100,525, fill = 'white')
buttonplusslashminus = drawpad.create_rectangle(50,462.5,100,487.5, fill = 'white')
buttonradicalx = drawpad.create_rectangle(50,425,100,450, fill = 'white')
buttonrdownarrow = drawpad.create_rectangle(50,387.5,100,412.5, fill = 'white')
buttonrslashs = drawpad.create_rectangle(50,350,100,375, fill= 'white')
#Big Arrows
buttonbigarrowup = drawpad.create_rectangle(287.5,337.5,337.5,363.5, fill = '#DCDCDE')
buttonbigarrowleft = drawpad.create_rectangle(237.5,350,275,400, fill = '#DCDCDE')
buttonbigarrowright = drawpad.create_rectangle(350,350,387.5,400, fill = '#DCDCDE')
buttonbigarrowdown = drawpad.create_rectangle(287.5,387.5,337.5,412.5, fill = '#DCDCDE')



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
	

		
										
                drawpad.bind("<Button-1>", self.click)

		drawpad.pack()
		
	def click(self, event):
            if drawpad.find_withtag(CURRENT):
                drawpad.itemconfig(CURRENT, fill="blue")
                drawpad.update_idletasks()
                drawpad.after(200)
                drawpad.itemconfig(CURRENT, fill="white")

myapp = MyApp(root)


root.mainloop()