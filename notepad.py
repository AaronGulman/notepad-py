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
        ('Assembly files', '*.asm'),
        ('Python files', '*.py')
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
        ('All supported files', '*.txt *.html *.css *.js *.java *.c *.cpp *.cs *.sh *.asm *.py'),
        ('Text files', '*.txt'),
        ('HTML files', '*.html'),
        ('CSS files', '*.css'),
        ('C files', '*.c'),
        ('C++ files', '*.cpp'),
        ('Java files', '*.java'),
        ('JavaScript files', '*.js'),
        ('C# files', '*.cs'),
        ('Bash files', '*.sh'),
        ('Assembly files', '*.asm'),
        ('Python files', '*.py')
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
    entry.tag_delete("function_name")
    entry.tag_delete("event_listener")
    entry.tag_delete("function_param")

    # Define keywords
    keywords = [
        'if', 'else', 'switch', 'case', 'default', 'break', 'continue', 'return',
        'throw', 'try', 'catch', 'finally', 'debugger',
        'for', 'while', 'do', 'for...in', 'for...of',
        'function', 'const', 'let', 'var', 'async', 'await',
        'class', 'extends', 'super', 'new', 'this', 'constructor', 'static',
        'get', 'set', 'yield', 'import', 'export', 'from', 'as', 'default',
        'throw', 'try', 'catch', 'finally',
        'true', 'false', 'null', 'undefined', 'NaN', 'Infinity', '-Infinity',
        'typeof', 'instanceof', 'delete', 'void', 'with',
        'enum', 'await', 'implements', 'interface', 'package', 'private',
        'protected', 'public', 'abstract', 'yield','alert','console.log'
    ]

    # Get the text content
    text = entry.get(1.0, END)

    # Match standalone keywords
    for keyword in keywords:
        pattern = rf'\b{keyword}\b'
        for match in re.finditer(pattern, text):
            start, end = match.span()
            if not is_inside_quotes(text, start):
                entry.tag_add("keyword", f"1.0+{start}c", f"1.0+{end}c")

    # Highlight addEventListener
    event_listener_pattern = re.compile(r'\baddEventListener\b')
    for match in event_listener_pattern.finditer(text):
        start, end = match.span()
        entry.tag_add("event_listener", f"1.0+{start}c", f"1.0+{end}c")

    # Highlight function names and usages
    highlight_functions_and_usages(text)

    # Highlight parentheses and curly braces
    highlight_parentheses_and_curly_braces(text)

    # Configure tags
    entry.tag_config("keyword", foreground='#6d32a8', font=('Roboto', 18, 'bold'))
    entry.tag_config("parenthesis", foreground='#FFD700')
    entry.tag_config("curly_braces", foreground='#FFD700')
    entry.tag_config("function_name", foreground='#FF4500', font=('Roboto', 18, 'bold'))
    entry.tag_config("event_listener", foreground='#FFD700', font=('Roboto', 18, 'bold'))
    entry.tag_config("function_param", foreground='#ADD8E6', font=('Roboto', 18))

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
    stack = []
    func_params = []

    def process_function_params(start, end):
        param_start = text.find('(', end)
        param_end = text.find(')', param_start)
        if param_start != -1 and param_end != -1:
            params_text = text[param_start+1:param_end]
            for param_match in re.finditer(r'\w+', params_text):
                param_start = param_match.start() + param_start + 1
                param_end = param_match.end() + param_start
                entry.tag_add("function_param", f"1.0+{param_start}c", f"1.0+{param_end}c")

    # Highlight parentheses and curly braces
    for index, char in enumerate(text):
        if char == '(':
            stack.append(index)
        elif char == ')':
            if stack:
                start = stack.pop()
                entry.tag_add("parenthesis", f"1.0+{start}c", f"1.0+{start+1}c")
                entry.tag_add("parenthesis", f"1.0+{index}c", f"1.0+{index+1}c")
        elif char == '{':
            stack.append(index)
        elif char == '}':
            if stack:
                start = stack.pop()
                entry.tag_add("curly_braces", f"1.0+{start}c", f"1.0+{start+1}c")
                entry.tag_add("curly_braces", f"1.0+{index}c", f"1.0+{index+1}c")
    
    # Highlight function parameters within parentheses
    function_pattern = re.compile(r'\bfunction\b\s*\w*\s*\(([^)]*)\)')
    for match in function_pattern.finditer(text):
        start, end = match.span()
        process_function_params(start, end)
    
    # Highlight function arguments in function calls
    function_call_pattern = re.compile(r'(\w+)\s*\(([^)]*)\)')
    for match in function_call_pattern.finditer(text):
        func_name, args = match.groups()
        args_start = match.start(2)
        args_end = match.end(2)
        for arg_match in re.finditer(r'\w+', args):
            arg_start = arg_match.start() + args_start
            arg_end = arg_match.end() + args_start
            entry.tag_add("function_param", f"1.0+{arg_start}c", f"1.0+{arg_end}c")

def highlight_functions_and_usages(text):
    # Highlight function names and their usages
    function_pattern = re.compile(r'\bfunction\s+(\w+)\s*\(.*?\)\s*{')
    function_names = set()

    # Find function declarations
    for match in function_pattern.finditer(text):
        func_name = match.group(1)
        function_names.add(func_name)
        start, end = match.span()
        entry.tag_add("function_name", f"1.0+{start}c", f"1.0+{end}c")
        opening_brace = text.find('{', end)
        if opening_brace != -1:
            entry.tag_add("curly_braces", f"1.0+{opening_brace}c", f"1.0+{opening_brace+1}c")

    # Highlight function usages
    for func_name in function_names:
        usage_pattern = re.compile(rf'\b{func_name}\b')
        for match in usage_pattern.finditer(text):
            start, end = match.span()
            if not is_inside_quotes(text, start):
                entry.tag_add("function_name", f"1.0+{start}c", f"1.0+{end}c")

root = Tk()
root.geometry('930x770')
root.title('Notepy')
root.config(bg='black')
root.resizable(False, False)

# Create the Text widget first
entry = Text(root, height='33', width='82', wrap=WORD, font=('Roboto', 18), fg='#18ab18', bg='#05021a')
entry.place(x=10, y=60)

# Enable undo functionality only
entry.config(undo=True)

# Bind keyboard shortcuts for undo and redo
root.bind('<Command-z>', lambda event: entry.edit_undo())
root.bind('<Command-Shift-z>', lambda event: entry.edit_redo())

# Create buttons after the Text widget
b1 = Button(root, width='20', height='2', bg='#fff', text='Save File', command=save_file)
b1.place(x=150, y=5)
b2 = Button(root, width='20', height='2', bg='#fff', text='Open File', command=open_file)
b2.place(x=550, y=5)

entry.bind('<KeyRelease>', on_text_change)  # Bind text change event for syntax highlighting

root.mainloop()
