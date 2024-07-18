from tkinter import *
from tkinter import filedialog


root = Tk()
root.geometry('600x600')
root.title('Notepy')
root.config(bg='black')
root.resizable(False,False)


def save_file():
        open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=[
                        ( 'text files','*.txt'),
                       ('HTML files','*.html'),
                      ( 'CSS files','*.css'),
                       ('C files','*.c'),
                      ( 'C++ files','*.cpp'),
                       ('JAVA files','*.java'),
                      ( 'JAVASCRIPT files','*.js'),
                      ( 'C# files','*.cs'),
                      ( 'C# files','*.csh')
        ])
        if open_file is None:
                return
        text=str(entry.get(1.0,END))
        open_file.write(text)
        open_file.close()

def open_file():
       file=filedialog.askopenfile(mode='r',filetypes=[
            ('All supported files', '*.txt *.html *.css *.js *.java *.c *.cpp *.csh *.cs'),
                      ( 'text files','*.txt'),
                       ('HTML files','*.html'),
                      ( 'CSS files','*.css'),
                       ('C files','*.c'),
                      ( 'C++ files','*.cpp'),
                       ('JAVA files','*.java'),
                      ( 'JAVASCRIPT files','*.js'),
                      ( 'C# files','*.cs'),
                      ( 'C# files','*.csh')
               ]
                                   )
       if file is not None:
               content=file.read()
               entry.insert(END, content)


b1 = Button(root,width='20',height='2',bg='#fff',text='save file',command=save_file).place(x=100,y=5)
b2 = Button(root,width='20',height="2",bg='#fff',text='open file',command=open_file).place(x=300,y=5)

entry=Text(root, height='33',width='82',wrap=WORD, font=('Times New Roman', 18))
entry.place(x=10,y=60)



root.mainloop()