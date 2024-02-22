from tkinter import*

root=Tk()
frame1= Frame(root,highlightbackground="black",highlightthickness=5)
frame1.pack()

frame2=Frame(root,highlightbackground="black",highlightthickness=5)
frame2.pack(side= "bottom" )

button1= Button(frame1,text="                   button1                               ")    #We are creating buttons inside this frame
button1.pack()

button2 = Button(frame2,text = "                button2                               ")
button2.pack()

root.geometry("500x500")
root.mainloop()