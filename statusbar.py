from tkinter import*
root=Tk()
statusbar=Label(root,text="the current status of the application ",bd=2,relief=SUNKEN,anchor=N)  # when we write 'sunken' it define he status bar 
statusbar.pack(side="bottom",fill=X)   #achor :desides the: east ,west, north, south; and  fill "x" comes on  x axis 
root.geometry("300x300")

root.mainloop()