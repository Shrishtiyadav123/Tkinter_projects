from tkinter import*
from tkinter.messagebox import showinfo

class Demo:
    def __init__(self,rootone) -> None:
        self.label = Label(rootone,text='text message')
        self.label.pack()

        self.button = Button(rootone,text='clickhere')
        self.button['command']=self.button_clicked
        self.button.pack()

    def button_clicked(self):
        print('text')

        showinfo (title='information',message='hello tkinter !')
        label = Label(root,text='user clicked information')
        label.pack()

root =Tk()
d = Demo(root)
root.geometry('300x300')
root.mainloop()