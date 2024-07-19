from tkinter import *
from tkinter import filedialog, messagebox

def save_file():
    open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=[
        ('Text files', '*.txt'),
        ('HTML files', '*.html'),
        ('CSS files', '*.css'),
        ('C files', '*.c'),
        ('C++ files', '*.cpp'),
        ('Java files', '*.java'),
        ('JavaScript files', '*.js'),
        ('C# files', '*.cs'),
        ('Bash files', '*.sh'),
        ('Assembly files', '*.asm')
    ])
    if open_file is None:
        return
    try:
        text = entry.get(1.0, END)
        open_file.write(text)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        open_file.close()

def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[
        ('All supported files', '*.txt *.html *.css *.js *.java *.c *.cpp *.cs *.sh *.asm'),
        ('Text files', '*.txt'),
        ('HTML files', '*.html'),
        ('CSS files', '*.css'),
        ('C files', '*.c'),
        ('C++ files', '*.cpp'),
        ('Java files', '*.java'),
        ('JavaScript files', '*.js'),
        ('C# files', '*.cs'),
        ('Bash files', '*.sh'),
        ('Assembly files', '*.asm')
    ])
    if file is not None:
        try:
            content = file.read()
            entry.delete(1.0, END)  # Clear existing content
            entry.insert(END, content)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            file.close()

def on_text_change(event):
    # Simple example to change text color based on keywords
    keywords = [
    #Control Flow Keywords
    'if', 'else', 'switch', 'case', 'default', 'break', 'continue', 'return', 
    'throw', 'try', 'catch', 'finally', 'debugger',
    
    #Looping Keywords
    'for', 'while', 'do', 'for...in', 'for...of',
    
    #Function Keywords
    'function', 'const', 'let', 'var', 'async', 'await',
    
    #Object and Array Keywords
    'class', 'extends', 'super', 'new', 'this', 'constructor', 'static', 
    'get', 'set', 'yield', 'import', 'export', 'from', 'as', 'default',
    
    #Error Handling Keywords
    'throw', 'try', 'catch', 'finally',
    
    #Boolean Keywords
    'true', 'false', 'null', 'undefined', 'NaN', 'Infinity', '-Infinity',
    
    #Miscellaneous Keywords
    'typeof', 'instanceof', 'delete', 'void', 'with',
    
    #Reserved Keywords (Future or current reserved in strict mode)
    'enum', 'await', 'implements', 'interface', 'package', 'private', 
    'protected', 'public', 'abstract', 'yield'
]
    for keyword in keywords:
        start = '1.0'
        while True:
            pos = entry.search(keyword, start, stopindex=END)
            if not pos:
                break
            end = f"{pos}+{len(keyword)}c"
            entry.tag_add(keyword, pos, end)
            entry.tag_config(keyword, foreground='36013F')
            start = end

root = Tk()
root.geometry('600x600')
root.title('Notepy')
root.config(bg='black')
root.resizable(False, False)

b1 = Button(root, width='20', height='2', bg='#fff', text='Save File', command=save_file)
b1.place(x=100, y=5)
b2 = Button(root, width='20', height='2', bg='#fff', text='Open File', command=open_file)
b2.place(x=300, y=5)

entry = Text(root, height='33', width='82', wrap=WORD, font=('Times New Roman', 18), bg='#808080')
entry.place(x=10, y=60)

entry.bind('<KeyRelease>', on_text_change)  # Bind text change event for syntax highlighting

root.mainloop()
