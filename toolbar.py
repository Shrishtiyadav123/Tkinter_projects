from tkinter import*
def function1():
    print("menu selected ")
root = Tk()

toolbar = Frame(root,bg="brown",bd=5)
insertbutton = Button(toolbar,text=" insertbutton",command= function1)
insertbutton1 = Button(toolbar,text=" insertbutton1",command= function1)
deletebutton = Button(toolbar,text="deletebutton",command=function1)
deletebutton1 = Button(toolbar,text="deletebutton1",command=function1)
insertbutton.pack(side=LEFT,padx=2,pady=5)
insertbutton1.pack(side=LEFT,padx=3,pady=4)
deletebutton.pack(side=RIGHT,padx=5,pady=2)
deletebutton1.pack(side=RIGHT,padx=3,pady=4)
toolbar.pack()
root.geometry("500x500")

root.mainloop()