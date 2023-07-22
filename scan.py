import os  
import get_directory
import filetype

def scan_files():
    dir=get_directory.get_directory()
    walker=os.walk(dir)
    res=[]
    inp=input("Press 1 using extension and 2 using file type : ")
    if(inp=='1'):
        filetyp=input("Enter The file Extension .")
        for folder,subfolder,files in walker:
            for file in files:
                filepath =os.path.join(folder,file)
                if(filepath.endswith("."+filetyp)):
                    res.append([file,filepath,os.stat(filepath).st_size])
        os.system("cls")
    elif (inp=='2'):
        os.system("cls")
        print("Press \n 1 for Image \n 2 for Video \n 3 for audio \n 4 for application : ")
        choice=input()
        if(choice=="1"):
            kind="image"
        elif (choice=="2"):
            kind="video"
        elif(choice=="3"):
            kind="audio"
        elif(choice=="4"):
            kind="application"
        else:
            print("Wrong Choice")
            return
        for folder,subfolder,files in walker:
            for file in files:
                dir=os.path.join(folder,file)
                knd=filetype.guess(dir)
                knd=knd.mime.split("/")[0]
                if(knd==kind):
                    res.append([file,dir,os.stat(dir).st_size])
        os.system("cls")

    else:
        print("Wrong choice")
        return 
    for info in res:
            print("File Name      : ",info[0])
            print("File Directory : ",info[1])
            if(info[2]>=2**30):
                size=str(info[2]//2**30)+" GB "+str((info[2]-(info[2]//2**30)*2**30)//2**20) +"MB"
            else:
                size=str(info[2]//2**20)+"MB"
            print("File Size      : ",size)
            print()
            if len(res)==0:
                print(f"NO FILE FOUND WITH .")