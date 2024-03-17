from tkinter import *
from tkinter import filedialog


root = Tk()
root.geometry('600x600')
root.title('Notepy')
root.config(bg='black')
root.resizable(False,False)

def save_file():
        print('')

def open_file():
        print('')


b1 = Button(root,width='20',height='2',bg='#fff',text='save file',command=save_file).place(x=100,y=5)
b2 = Button(root,width='20',height="2",bg='#fff',text='open file',command=open_file).place(x=300,y=5)


root.mainloop()