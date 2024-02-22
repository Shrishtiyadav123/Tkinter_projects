from tkinter import *
def display():
    label2 = Label(root,text ="welcome shrishti ",fg='purple',bg='grey',font=('arial',14))
    label2.pack() 

def show():
    data= entry.get()
    print(data)
    label1 = Label(root,text =data)
    label1.pack() 
root = Tk()
root.geometry('400x400')

label1 = Label(root,text ="python class",fg='purple',bg='grey',font=('arial',14))
label1.pack()  #pack is compulsory

button1=Button(root,text='click',command=display)
button1.pack()

button2=Button(root,text='click me',command=show)
button2.pack()


entry=Entry(root)
entry.pack()


root.mainloop()
#Lable is use to print 
