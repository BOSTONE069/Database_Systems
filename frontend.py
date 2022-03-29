from tkinter import *

win = Tk()

l1 = Label(win, text='Date')
l1.grid(row=0,column=0)
l2 = Label(win, text='Earnings')
l2.grid(row=0,column=2)
l3 = Label(win, text='Excercise')
l3.grid(row=1,column=0)
l4 = Label(win, text='Study')
l4.grid(row=1,column=2)
l5 = Label(win, text='Diet')
l5.grid(row=2,column=0)
l6 = Label(win, text='Python')
l6.grid(row=2,column=2)

date_text = StringVar()
e1 = Entry(win, textvariable=date_text)
e1.grid(row=0,column=1)

earnings_text = StringVar()
e1 = Entry(win, textvariable=earnings_text)
e1.grid(row=0,column=1)

excercise_text = StringVar()
e1 = Entry(win, textvariable=excercise_text)
e1.grid(row=0,column=1)

study_text = StringVar()
e1 = Entry(win, textvariable=study_text)
e1.grid(row=0,column=1)

diet_text = StringVar()
e1 = Entry(win, textvariable=diet_text)
e1.grid(row=0,column=1)

python_text = StringVar()
e1 = Entry(win, textvariable=python_text)
e1.grid(row=0,column=1)



win.mainloop()
