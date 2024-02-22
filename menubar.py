from tkinter import*
def donothing():
    print("button selected ")
    button = Button(text=("do nothing" ))
    button.pack()
root = Tk()
menubar= Menu(root)  #to creat menu,  use menu 
filemenu = Menu(menubar,tearoff=0)  #tearoff: means it dosent make the dash dash lines 
filemenu.add_command(label = "New",command= donothing)  #to add options in menu use: add_command ; click : file then : new,open,save, etc ayega  
filemenu.add_separator()
filemenu.add_command(label = "Open",command= donothing)
filemenu.add_separator()
filemenu.add_command(label = "Save",command= donothing)
filemenu.add_command(label = "Saveas",command= donothing)
filemenu.add_separator()
filemenu.add_command(label = "Close",accelerator="alt+f4" , command= donothing)

menubar.add_cascade(label="file",menu=filemenu)  #add_cascade : to add more new options like : file , edit,selection etc 

editmenu = Menu(menubar,tearoff=0)
editmenu.add_command(label="undo",accelerator= 'cntrl+ U' , command=donothing)
editmenu.add_command(label="redo",command=donothing)
editmenu.add_separator()
editmenu.add_command(label="cut",command=donothing)
editmenu.add_command(label="copy",command=donothing)
editmenu.add_command(label="paste",command=donothing)
editmenu.add_separator()

menubar.add_cascade(label="Edit",menu=editmenu)

selectionbar=Menu(menubar,tearoff=0)
selectionbar.add_command(label='select all',accelerator="ctrl + A",command=donothing)
selectionbar.add_command(label='Expand selection',accelerator="shift+alt+right arrow", command=donothing)
selectionbar.add_command(label='shrink selection',accelerator='shift+alt=left arrow',command=donothing)
selectionbar.add_separator()
selectionbar.add_command(label="copy line up",accelerator='shift+alt+uparrow',command=donothing)
selectionbar.add_command(label='copy line down ',accelerator='sift+alt+downarrow',command=donothing)
selectionbar.add_command(label='move line up',accelerator='shift+uparrow',command=donothing)
selectionbar.add_command(label='move line down',accelerator='shift+downarrow',command=donothing)
selectionbar.add_command(label='duplicate selection',command=donothing)

menubar.add_cascade(label='Selection',menu=selectionbar)

viewbar=Menu(menubar,tearoff=0)
viewbar.add_command(label='command pallete',accelerator='ctrl+shift+p',command=donothing)
menubar.add_cascade(label='view',menu=viewbar)


root.config(menu=menubar)   # to show the results use : root.config 
root.geometry("300x300")
root.mainloop()

#********************************************************************************************************************************
