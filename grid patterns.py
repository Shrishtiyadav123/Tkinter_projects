
from tkinter import *
root= Tk()
frame= Frame(root)

for x in range(3):
    for y in range(3):
        frame= Frame(root)
        frame.grid(row= x,column=y)
        button= Button(frame,text= f"row{x} \n column{y}")
        button.pack(padx=5,pady=4)

root.mainloop()