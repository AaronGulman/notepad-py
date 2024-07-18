# Notepad Application

## Technologies Used
- Python
- Tkinter
- PyInstaller

## Overview
The Notepad Application project is a simple text editor built with Python and Tkinter. It allows users to create, open, edit, and save text files. The application is packaged using PyInstaller to create an executable file.

## Directory Structure
```

├── build / notepad
├── dist
│ └── notepad.exe
├── notepad.py
├── notepad.spec

```


## Project Files
1. **notepad.py**: Main Python script for the Notepad application. Implements the GUI and functionality for creating, opening, editing, and saving text files using Tkinter.
2. **notepad.spec**: PyInstaller specification file used to create the executable. Defines the configuration for building the `notepad.exe` file.
3. **dist/notepad.exe**: The generated executable file for the Notepad application.

## Usage
1. Clone the repository.
2. Ensure you have Python installed on your system.
3. Navigate to the project directory.
4. Run the following command to install the required dependencies:

- ```pip install tk```

5. To run the application, execute the following command:
python notepad.py

6. To create an executable file, use PyInstaller with the provided `notepad.spec` file:
pyinstaller notepad.spec

7. The executable file `notepad.exe` will be generated in the `dist` directory.
