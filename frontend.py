from tkinter import *

def get_selected_row():
    pass

win = Tk()
 
win.wm_title('MY ROUTINE DATABSE')

#This is for defining the labels of the systems
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

#This is for defining the data entry boxes in the system
date_text = StringVar()
e1 = Entry(win, textvariable=date_text)
e1.grid(row=0,column=1)

earnings_text = StringVar()
e2 = Entry(win, textvariable=earnings_text)
e2.grid(row=0,column=3)

excercise_text = StringVar()
e3 = Entry(win, textvariable=excercise_text)
e3.grid(row=1,column=1)

study_text = StringVar()
e4 = Entry(win, textvariable=study_text)
e4.grid(row=1,column=3)

diet_text = StringVar()
e5 = Entry(win, textvariable=diet_text)
e5.grid(row=2,column=1)

python_text = StringVar()
e6 = Entry(win, textvariable=python_text)
e6.grid(row=2,column=3)

list = Listbox(win,height=8,width=35)
list.grid(row=3,column=0,rowspan=9,columnspan=2)

sb = Scrollbar(win)
sb.grid(row=3,column=2,rowspan=9)


list.bind('<<ListboxSelection>>',get_selected_row)

#This is for defining the buttons to be used in the project        
b1 = Button(win,text='ADD',width=12,pady=5)
b1.grid(row=3,column=3)

b2 = Button(win,text='Search',width=12,pady=5)
b2.grid(row=4,column=3)

b3 = Button(win, text='Delete Date', width=12, pady=5)
b3.grid(row=5, column=3)

b4 = Button(win, text='View All', width=12, pady=5)
b4.grid(row=6, column=3)

b5 = Button(win,text='Close',width=12,pady=5,command = win.destroy)
b5.grid(row=7,column=3)
    
win.mainloop()
