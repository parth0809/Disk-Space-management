from tkinter import Tk 
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilenames,askopenfilename
  
Tk().withdraw()# to avoid full window 

def get_directory():
    path=askdirectory(title="Select a folder")
    return str(path)

def get_files():
    path=askopenfilenames(title="Select A files")
    return path

def get_file():
    path=askopenfilename(title="Select a File")
    return path
    