'''a = 5
for i in (range (1,a)):
    for j in range(i+1):
        print(j, end="")
    print('')'''


import tkinter
from tkinter import*
import scipy
from scipy import constants
x=Tk()
x.geometry('500x200')
input1=Label(x,text='Enter radius:').grid(column=0,row=0)
entry1=Entry()
entry1.grid(column=1,row=0,columnspan=3)
input2=Label(x,text='Enter length of the side:').grid(column=0,row=1)
entry2=Entry()
entry2.grid(column=1,row=1,columnspan=3)
def calculate(operation):
    try:
        radius=float(entry1.get())
        side=float(entry2.get())

        if operation=='circle':
            result=(constants.pie)*radius**2
        elif operation=='square':
            result=side**2

        results.config(text=f"Area of {operation} is {result}")
    except ValueError:
        results.config(text="Invalid input! Please enter numbers only")

circlebutton=CheckButton(x, text='circle', onvalue=1, offvalue=0, height=2,
                         width=10,command=lambda:calculate('circle')).grid(pady=
                                                                5,sticky='ew')
squarebutton=CheckButton(x,text='square', onvalue=1,offvalue=0, height=2,
                         width=10,command=lambda:calculate('square')).grid(pady=
                                                                5,sticky='ew')
results=Label(x,text="Result:")
results.grid(column=0, row=3, columnspan=3, pady=5,padx=5,sticky='ew')

x.mainloop()
