from tkinter import *
root = Tk()
#Create a label Widget
myLabel1 = Label(root, text="Hellow World1!")
myLabel2 = Label(root, text="Hellow World2!")
#Shoving it into the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=2, column=0)
root.mainloop()