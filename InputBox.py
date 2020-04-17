from tkinter import *
#Must be before code
root = Tk()

def myClick():
    myLabel = Label(root, text=entryBox.get()).pack()

entryBox = Entry(root, width=50, bg="blue", fg="white", borderwidth=5)
entryBox.pack()
entryBox.insert(0, 'enter here')
myButton = Button(root, text="Enter data", padx= 50, pady=100, fg="blue", bg="red", command=myClick).pack()





#Must be last piece of code
root.mainloop()