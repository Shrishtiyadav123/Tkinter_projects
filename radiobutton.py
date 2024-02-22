from tkinter import *
root=Tk()
root.geometry("500x500")   #A checkbox comes from a button.

fuel= StringVar(value="petrol")  #string"VAR" : because it should be selected by default  
radio1= Radiobutton(root,text="petrol",variable=fuel,value="petrol")
radio2= Radiobutton(root,text="deisel",variable=fuel,value="deisel")
radio3= Radiobutton(root,text="electrical",variable=fuel,value="electrical")


radio1.pack()
radio2.pack()
radio3.pack()

root.mainloop()