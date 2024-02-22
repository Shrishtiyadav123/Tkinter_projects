from tkinter import*
def nothing():
    print('button pressed')
    button=Button(text=("nothing"))
    button.pack()
root= Tk()
menubar=Menu(root)  
filebar=Menu(menubar,tearoff= 0)
filebar.add_command(label='New tab',accelerator='cntrl+N',command=nothing)
filebar.add_command(label='New window',accelerator='cntrl+shift+N' ,command=nothing)
filebar.add_command(label='Open',accelerator='cntrl+O' ,command=nothing)
filebar.add_command(label='Save',accelerator='cntrl+S' ,command=nothing)
filebar.add_command(label='Save As',accelerator='cntrl+shift+S' ,command=nothing)
filebar.add_command(label='Save All',accelerator='cntrl+Alt+S' ,command=nothing)
filebar.add_separator()
filebar.add_command(label='Page setup',command=nothing)
filebar.add_command(label='Print',accelerator='cntrl+P' ,command=nothing)
filebar.add_separator()
filebar.add_command(label='close tab',accelerator='cntrl+W',command=nothing)
filebar.add_command(label='close window',accelerator='cntrl+shift+W',command=nothing)
filebar.add_command(label='Exit',command=nothing)
menubar.add_cascade(label='File',menu=filebar)

Editbar=Menu(menubar,tearoff=0)
Editbar.add_command(label="Undo",accelerator='cntrl+Z',command=nothing)
Editbar.add_separator()
Editbar.add_command(label='Cut',accelerator='cntrl+x',command=nothing)
Editbar.add_command(label='Copy',accelerator='cntrl+C',command=nothing)
Editbar.add_command(label='Paste',accelerator='cntrl+V',command=nothing)
Editbar.add_command(label='Delete',accelerator='Del',command=nothing)
Editbar.add_separator()
Editbar.add_command(label='Find',accelerator='cntrl+F',command=nothing)
Editbar.add_command(label='Find Next',accelerator='F3',command=nothing)
Editbar.add_command(label='Find Previous',accelerator='cntrl+F3',command=nothing)
Editbar.add_command(label='Replace',accelerator='cntrl+H',command=nothing)
Editbar.add_command(label='Go To',accelerator='cntrl+G',command=nothing)
Editbar.add_separator()
Editbar.add_command(label='Select All',accelerator='cntrl+A',command=nothing)
Editbar.add_command(label='Time/Date',accelerator='F5',command=nothing)
Editbar.add_separator()
Editbar.add_command(label='Font',command=nothing)
menubar.add_cascade(label='Edit',menu=Editbar)

Viewbar=Menu(menubar,tearoff=0)
Viewbar.add_command(label='Zoom',command=nothing)
Viewbar.add_command(label='Status bar',command=nothing)
Viewbar.add_command(label='Word wrap',command=nothing)
menubar.add_cascade(label='View',menu=Viewbar)

root.config(menu=menubar)
root.geometry('500x500')
root.mainloop()
