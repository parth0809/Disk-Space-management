import amt_space
import get_directory
import os
import duplicate
import delete_files
import large
import specs
import scan
import comdecom
def runapp():
    while(True):
        os.system("cls")
        print("Welcome to Disk Manager : ")
        print(" 1 for Space available in root directory \n 2 for Space used in root directory\n 3 to detect duplicates \n 4 for deleting files \n 5 to delete folders \n 6 to find large files in a directory \n 7 for Space Utiliztion specs\n 8 for Finding Specific files \n 9 for Deleting files with given extension \n 10 to Find a file Duplicates \n 11 for Compressing file \n 12 for Closing the appliction")
        print()
        a=(input("Enter You Selection : "))
        print()
        if(a=='1'):
            print("Current Directory : "+os.getcwd()[:3])
            print("Space available : ",amt_space.space_availabe("/"))
            print()
            input("press any key to continue: ")
            print()
        elif(a=='2'):
            print("Current Directory : "+os.getcwd()[:3])
            print("Space used : ",amt_space.space_used("/"))
            print()
            input("press any key to continue: ")
            print()
        elif(a=='3'):
            path=(get_directory.get_directory())
            try:
                unique_file,duplicates=duplicate.find_duplicates(path)
                for file in unique_file:
                    if(len(duplicates[file])>=1):
                        print("duplicates of : ",unique_file[file])
                        print()
                        for val in duplicates[file]:
                            print(val) 
                        print()
                        a=input("Do you want to delete duplicates ?y/n ").lower()
                        print()
                        if(a=='y'):
                            for file in unique_file:
                                for path in duplicates[file]:
                                    print(path)
                                    delete_files.delete_file(path)
                    else:
                        print(f"No duplicates of {unique_file[file]}")
            except:
                print("Permisson denied")
           
            print()
            input("press any key to continue: ")
            print()    
        elif(a=='4'):
            path=get_directory.get_files()
            try:
                for file in path:
                    delete_files.delete_file(file)
            except:
                print("No Files found ")
            print()
            input("press any key to continue: ")
            print()    
        elif(a=='5'):
            path=get_directory.get_directory()
            try:
                delete_files.removedir(path)
            except:
                print("No directory found")
            print()
            input("press any key to continue: ")
            print() 
        elif(a=='6'):
            path=get_directory.get_directory()
            try:
                large_file=large.large_files(path)
                for files in large_file:
                    print(files[0])
                if(input("Do You want to compress Files ? (y/n) ")=='y'):
                    for file in large_file:
                        if(input(f"compress {file} ? (y/n) ")=='y'):
                            try:
                                comdecom.compress(file[0])
                                print(f"{file}  Compressed Succesfully ")
                            except:
                                print(f"{file} Can't be compressed ")
            except:
                print("No directory found")
                
            print()
            input("press any key to continue: ")
            print() 
        elif(a=='7'):
            specs.getdetail()
            print()
            input("press any key to continue: ")
            print() 
        elif(a=='8'):
            
            try:
                scan.scan_files()
            except:
                print("No extension Selected")
            print()
            input("press any key to continue: ")
            print() 
        elif(a=='9'):
            filepath=get_directory.get_directory()
            ext=input("Enter the file extension .")
            try:
                delete_files.delete_file_with_ext(filepath,ext)
            except:
                print("no extension or no path selected")
            print()
            input("press any key to continue: ")
            print() 
        elif(a=='10'):
            filepath=get_directory.get_file()
            filedir=get_directory.get_directory()
            try:
                duplicates=duplicate.find_duplicates_of_file(filedir,filepath)
                print("Duplicates of : ",filepath )
                for file in duplicates:
                    print(file)
            except:
                print("Directory Not accessed . ")
            if((input("Do you want to delete files ? (y/n) ").lower())=='y'):
                for dup_files in duplicates:
                    delete_files.delete_file(dup_files)
            print()
            input("press any key to continue: ")
            print()
        elif(a=='11'):
            filepath=get_directory.get_file()
            var=input("Enter 1 for compressing and 2 for decompressing : " )
            if(var=='1'):
                try:
                    comdecom.compress(filepath)
                    print("File Compressed Succesfully ")
                except:
                    print("Can't be compressed ")
            elif(var=='2'):
                try:
                   comdecom.decompress(filepath)
                except:
                    print("cannot be decompressed. ")
            else:
                print("Wrong Choice")
            print()
            input("press any key to continue: ")
            print()
        elif(a=="12"):
            os.system("cls")
            print("Application closed  ")
            break
        else:
            continue


if __name__ =="__main__":
    runapp()