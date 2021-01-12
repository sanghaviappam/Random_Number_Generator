from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Random Number Generator")
root.resizable(False,False)
root.configure(bg='gray')
root.grid()

def randnum(event):
	import random
	value =random.randint(1,2000)
	print(value)
	updateDisplay(value)

def updateDisplay(myString):
	displayVariable.set(myString)


button_1=Button(root, text="Click For Random Number", width=30, height=5, compound="c",font=('times',13,'bold'),bg='white')
button_1.place(anchor=CENTER)

button_1.place(x=400,y=400)
button_1.bind("<Button-1>",randnum)

button_1.pack()
displayVariable = StringVar()
displayLabel = Label(root, textvariable=displayVariable,font=('times',20,'bold'),bg='yellow')
displayLabel.place(x=30,y=250)

displayLabel.pack()
root.mainloop()