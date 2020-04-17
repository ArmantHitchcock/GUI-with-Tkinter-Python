from tkinter import *
root = Tk()
Turnover = 4046321
CostOfGoods = 3941250
GrossProfit = Turnover - CostOfGoods
Wages = 20000
Stationary = 2000
Fual = 5000
Advertising = 6000
Expenses = Wages + Stationary + Fual + Advertising
NetProfitBefore = GrossProfit - Expenses
InterestIncome = 1200
Tax = round((NetProfitBefore + InterestIncome) * 0.28, 2)
NetProfit = round((NetProfitBefore + InterestIncome) - Tax, 2)

#Create a label Widget
myLabel1 = Label(root, text="Turnover").grid(row=0, column=0)
myLabel2 = Label(root, text="Cost of goods")
myLabel3 = Label(root, text="Gross Profit")
myLabel4 = Label(root, text="Expenses")
myLabel5 = Label(root, text="Wages")
myLabel6 = Label(root, text="Stationary")
myLabel7 = Label(root, text="Fual")
myLabel8 = Label(root, text="Advertising")
myLabel9 = Label(root, text="Net Profit Before")
myLabel10 = Label(root, text="Interest income")
myLabel11 = Label(root, text="Tax")
myLabel12 = Label(root, text="Net Profit")

myLabel21 = Label(root, text=f"{Turnover}")
myLabel22 = Label(root, text=f"{CostOfGoods}")
myLabel23 = Label(root, text=f"{GrossProfit}")
myLabel24 = Label(root, text=f"{Expenses}")
myLabel25 = Label(root, text=f"{Wages}")
myLabel26 = Label(root, text=f"{Stationary}")
myLabel27 = Label(root, text=f"{Fual}")
myLabel28 = Label(root, text=f"{Advertising}")
myLabel29 = Label(root, text=f"{NetProfitBefore}")
myLabel30 = Label(root, text=f"{InterestIncome}")
myLabel31 = Label(root, text=f"{Tax}")
myLabel32 = Label(root, text=f"{NetProfit}")
#Shoving it into the screen
#myLabel1
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=2, column=0)
myLabel4.grid(row=3, column=0)
myLabel5.grid(row=4, column=0)
myLabel6.grid(row=5, column=0)
myLabel7.grid(row=6, column=0)
myLabel8.grid(row=7, column=0)
myLabel9.grid(row=8, column=0)
myLabel10.grid(row=9, column=0)
myLabel11.grid(row=10, column=0)
myLabel12.grid(row=11, column=0)

myLabel21.grid(row=0, column=1)
myLabel22.grid(row=1, column=1)
myLabel23.grid(row=2, column=1)
myLabel24.grid(row=3, column=1)
myLabel25.grid(row=4, column=1)
myLabel26.grid(row=5, column=1)
myLabel27.grid(row=6, column=1)
myLabel28.grid(row=7, column=1)
myLabel29.grid(row=8, column=1)
myLabel30.grid(row=9, column=1)
myLabel31.grid(row=10, column=1)
myLabel32.grid(row=11, column=1)
root.mainloop()