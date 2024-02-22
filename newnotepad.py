from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename   #A file dialog is used to save it when we save a file. 
import os

root=Tk()
root.title('Shrishti notepad')
root.wm_iconbitmap('notes.png')   #wm_iconbitmap: this helps in pasting image; and  notes.png : is the name of the image 
root.geometry("500x500")
textarea=Text(root,font='simsun',undo=True)
file=None
textarea.pack(fill=BOTH,expand=True)


def cut():
    textarea.event_generate(('<<cut>>'))

def copy():
    textarea.event_generate(("<<copy>>"))

def paste():
    textarea.event_generate(("<<paste>>"))


def new_file():
    global file 
    root.title("shrishti - notepad")
    file= None
    textarea.delete('1.0',END)   #this is default 

def openfile():
    global file
    file= asksaveasfilename(defaultextension=".txt",filetypes=[("All file","*.*"),("Text document",".txt")]) #
    if file== "":   #if we keep it empty  
       file= None   #so it will come none 
    else:
        root.title(os.path.basename(file)+"-Notepad")   #file name and  concatinate notepad
        textarea.delete('1.0',END)
        f= open(file,"r")  #we have to open it in read mode thatsd why  r 
        textarea.insert("1.0",f.read())   
        f.close()   #f file will close 

def saveFile():
    global file
    file=asksaveasfilename(initialfile="untitled.txt",filetypes=[("all file","*.*")("text document",".txt")])  #initialfile : we we save our file without  any name so it gets save as untitled
    if file=="":
        file = None
    else:
    #to save the file
        f= open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()

    root.title(os.path.basename(file)+"-Notepad ")   #file's name and  -notepad  it will show 








menubar=Menu(root)  
filebar=Menu(menubar,tearoff= 0)
filebar.add_command(label='New',accelerator='cntrl+N',command=new_file)
filebar.add_command(label='Open',accelerator='cntrl+O' ,command=openfile)
# filebar.add_command(label='Save',accelerator='cntrl+S' ,command=saveFile)
# filebar.add_command(label='Save As',accelerator='cntrl+shift+S' ,command=saveFile)
# filebar.add_separator()
# filebar.add_command(label='close',accelerator='cntrl+W',command=root.quit)
# filebar.add_command(label='Exit',command=root.quit)
menubar.add_cascade(label='File',menu=filebar)

Editbar=Menu(menubar,tearoff=0)
Editbar.add_command(label='Cut',accelerator='cntrl+x',command=cut)
Editbar.add_command(label='Copy',accelerator='cntrl+C',command=copy)
Editbar.add_command(label='Paste',accelerator='cntrl+V',command=paste)
menubar.add_cascade(label='Edit',menu=Editbar)

# helpmenu=Menu(menubar,tearoff=0)
# helpmenu.add_command(label='help index',command=about)
# helpmenu.add_command(label='about....',command=about)
# menubar.add_cascade(label='help',menu=helpmenu)

root.config(menu=menubar)


root.mainloop()