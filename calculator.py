#creator aditya
from tkinter import *

rootwindow = Tk()

rootwindow.geometry('600x400')
rootwindow.title("Calculator")
rootwindow.resizable(0,0)

first_num = IntVar()
second_num = IntVar()

def addition():
    global rest
    f_1 =  (first_num.get())
    f_2 =  (second_num.get())
    res = f_1 + f_2
    rest =Label(rootwindow, text=res,font='arial 36 bold')
    rest.place(x=10,y=300)

def Division():
    global rest
    f_1 =  (first_num.get())
    f_2 =  (second_num.get())
    res = f_1 / f_2
    rest = Label(rootwindow, text=res,font='arial 36 bold')
    rest.place(x=10,y=300)



def Subtraction():
    global rest
    f_1 =  (first_num.get())
    f_2 =  (second_num.get())
    res = f_1 - f_2
    rest = Label(rootwindow, text=res,font='arial 36 bold')
    rest.place(x=10,y=300)

def Multiplication():
    global rest
    f_1 =  (first_num.get())
    f_2 =  (second_num.get())
    res = f_1 * f_2
    rest = Label(rootwindow, text=res,font='arial 36 bold')
    rest.place(x=10,y=300)

def clear():
    rest.destroy()
    first_entry.delete(0, END)
    second_entry.delete(0, END)

def exit():
    rootwindow.quit()

first_entry = Entry(rootwindow, width=40, textvariable=first_num)
first_entry.place(x= 300 , y= 50)
second_entry = Entry(rootwindow, width= 40, textvariable=second_num)
second_entry.place(x= 300 , y= 80)

Label(rootwindow, text= 'Enter first number',font='arial 15 bold').place(x= 100, y= 40)
Label(rootwindow,text= "Enter second number",font= 'arial 15 bold').place( x= 80 , y= 80)
Button(rootwindow, text="+",command=addition,width=10,height=5).place( x= 400 , y= 110)
Button(rootwindow, text="clear",command=clear,width=10,height=5).place( x= 300 , y= 110)
Button(rootwindow, text="-",command=Subtraction,width=10,height=5).place( x= 300 , y= 210)
Button(rootwindow, text="x",command=Multiplication,width=10,height=5).place( x= 400 , y= 210)
Button(rootwindow, text="/",command=Division,width=10,height=5).place( x= 500 , y= 110)
Button(rootwindow, text="EXIT",command=exit,width=10,height=5).place( x= 500 , y= 210)





rootwindow.mainloop()




