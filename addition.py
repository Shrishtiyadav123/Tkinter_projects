from tkinter import *  #star means all 
def add():
    n1 = int(num1.get())
    n2 = int(num2.get())
    # print(n1+n2)
    result = str(n1+n2)
    answer.config(text='answer is:'+result)

def sub():
    n1 = int(num1.get())
    n2 = int(num2.get())
    # print(n1+n2)
    result = str(n1-n2)
    answer.config(text='answer is:'+result)

def multi():
    n1 = int(num1.get())
    n2 = int(num2.get())
    # print(n1+n2)
    result = str(n1*n2)
    answer.config(text='answer is:'+result)

def div():
    n1 = int(num1.get())
    n2 = int(num2.get())
    # print(n1+n2)
    result = str(n1/n2)
    answer.config(text='answer is:'+result)
root = Tk()  
root.geometry("300x300")   #this decides the height and the width 

num1 = Entry(root)
num2 = Entry(root)

num1.pack()
num2.pack()

button = Button(root,text="add",command= add)
button.pack(side= "left")

button = Button(root,text="sub",command= sub)
button.pack(side = "right")

button = Button(root,text="multiply",command= multi)
button.pack(side = "top") 

button = Button(root,text="div",command= div)
button.pack(side ="bottom")
answer = Label(root)
answer.pack()
root.mainloop()   #this helps in opening the window 
#***************************************
from tkinter import *
def add():
    a1=(a.get())
    b1=(b.get())
    result=str(a1+b1)
    answer.config(text="the ans of this will be "+result)
root=Tk()
root.geometry("500x500")
a=Entry(root,fg="black",font="caligraphy")
b=Entry(root,fg="black",font="caligraphy")
a.pack()
b.pack()
button=Button(root,text="login",command= add)
button.pack()
answer= Label(root)
answer.pack()
root.mainloop()