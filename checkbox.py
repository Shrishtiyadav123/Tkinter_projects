from tkinter import *

def selected():
    label.config(text=check_value.get())
root= Tk()
root.geometry("500x500")

check_value=BooleanVar()   #booleanvar sets 0 or 1 value  
checkbutton1 = Checkbutton(root,text="accept term ",variable =check_value,command=selected )
checkbutton1.pack()
label = Label(root)
label.pack()
root.mainloop()

