from tkinter import *
#Must be before code
root = Tk()

def myClick():
    myLabel = Label(root, text="Clicked the button").pack()
'''
defining a button with 
padding on the sides of 50 and 
padding on the top and bottom of 100, 
font colour og blue , 
background colour of red and
action on click to print a label
'''
myButton = Button(root, text="Click", padx= 50, pady=100, fg="blue", bg="red", command=myClick)

myButton.pack()

#Must be last piece of code
root.mainloop()