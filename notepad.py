from tkinter import *
from tkinter import filedialog, messagebox
import re

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
    # Clear previous tags
    entry.tag_delete("keyword")
    entry.tag_delete("parenthesis")
    entry.tag_delete("curly_braces")

    # Define keywords
    keywords = [
        # Control Flow Keywords
        'if', 'else', 'switch', 'case', 'default', 'break', 'continue', 'return',
        'throw', 'try', 'catch', 'finally', 'debugger',

        # Looping Keywords
        'for', 'while', 'do', 'for...in', 'for...of',

        # Function Keywords
        'function', 'const', 'let', 'var', 'async', 'await',

        # Object and Array Keywords
        'class', 'extends', 'super', 'new', 'this', 'constructor', 'static',
        'get', 'set', 'yield', 'import', 'export', 'from', 'as', 'default',

        # Error Handling Keywords
        'throw', 'try', 'catch', 'finally',

        # Boolean Keywords
        'true', 'false', 'null', 'undefined', 'NaN', 'Infinity', '-Infinity',

        # Miscellaneous Keywords
        'typeof', 'instanceof', 'delete', 'void', 'with',

        # Reserved Keywords (Future or current reserved in strict mode)
        'enum', 'await', 'implements', 'interface', 'package', 'private',
        'protected', 'public', 'abstract', 'yield'
    ]

    # Get the text content
    text = entry.get(1.0, END)

    # Match standalone keywords
    for keyword in keywords:
        pattern = rf'\b{keyword}\b'  # Word boundary to ensure standalone
        for match in re.finditer(pattern, text):
            start, end = match.span()
            # Ensure not inside quotes
            if not is_inside_quotes(text, start):
                entry.tag_add("keyword", f"1.0+{start}c", f"1.0+{end}c")
    
    # Highlight parentheses and curly braces
    highlight_parentheses_and_curly_braces(text)

    # Configure tags
    entry.tag_config("keyword", foreground='#6d32a8', font=('Times New Roman', 18, 'bold'))
    entry.tag_config("parenthesis", foreground='#FFD700')
    entry.tag_config("curly_braces", foreground='#FFD700')

def is_inside_quotes(text, index):
    # Check if the index is inside quotes
    quote_chars = ['"', "'"]
    in_quotes = False
    for char_index, char in enumerate(text):
        if char in quote_chars:
            in_quotes = not in_quotes
        if char_index == index:
            return in_quotes
    return False

def highlight_parentheses_and_curly_braces(text):
    # Patterns to find function declarations and their parentheses
    function_pattern = re.compile(r'\bfunction\b\s*\w*\s*\(([^)]*)\)')
    for match in function_pattern.finditer(text):
        start, end = match.span()
        # Highlight parentheses
        for i in range(start, end):
            if text[i] in '()':
                entry.tag_add("parenthesis", f"1.0+{i}c", f"1.0+{i+1}c")

    # Highlight curly braces
    for index, char in enumerate(text):
        if char in '{}':
            entry.tag_add("curly_braces", f"1.0+{index}c", f"1.0+{index+1}c")

root = Tk()
root.geometry('600x600')
root.title('Notepy')
root.config(bg='black')
root.resizable(False, False)

b1 = Button(root, width='20', height='2', bg='#fff', text='Save File', command=save_file)
b1.place(x=100, y=5)
b2 = Button(root, width='20', height='2', bg='#fff', text='Open File', command=open_file)
b2.place(x=300, y=5)

entry = Text(root, height='33', width='82', wrap=WORD, font=('Times New Roman', 18), bg='#070630')
entry.place(x=10, y=60)

entry.bind('<KeyRelease>', on_text_change)  # Bind text change event for syntax highlighting

root.mainloop()
