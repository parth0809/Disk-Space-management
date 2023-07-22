import os 
import shutil

def delete_file(path):
    if(input(f"Do you want to delete file in {path} ? y/n ").lower()=='y'):
        os.remove(path)
        print(f"File at path {path} deleted succesfully")
        print()
def removedir(path):
    if(input(f"Do you want to delete folder in {path} ? y/n ").lower()=='y'):
        shutil.rmtree(path,ignore_errors=True,onerror="omitted")
        print(f"{path} removed")
        print()
def delete_file_with_ext(path,ext):
    dir=os.listdir(path)
    for file in dir:
        filepath=os.path.join(path,file)
        if (filepath.endswith("."+ext)):
            delete_file(filepath)
