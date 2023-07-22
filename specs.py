import shutil
import psutil
import os
import get_directory

def getdetail():
    os.system("cls")
    print("Breakdown of space utilization : ")
    print(" 1 on basis of drives \n 2 on basis of path \n 3 on basis of type of file ")
    a=int(input("Enter Your choice : "))
    if(a==1):
        os.system("cls")
        for device in psutil.disk_partitions():
            data=shutil.disk_usage(device[0])
            print("Device : ",device[0],"\n")
            print (f"Total space in drive {device[0]} : {data[0]//2**30} GB")
            print (f"Used space in drive {device[0]} : {data[1]//2**30} GB")
            print (f"Free space availabe in drive {device[0]} : {data[2]//2**30} GB")
            print("")
    elif(a==2):
        os.system("cls")
        path=get_directory.get_directory()
        total_space=0
        walker=os.walk(path)
        fileinfo=[]
        for folder,subfolder,files in walker:
            for file in files:
                filepath=os.path.join(folder,file)
                total_space+=os.stat(filepath).st_size
                fileinfo.append([filepath,os.stat(filepath).st_size])
        if(total_space>=2**30):
            print(f"Total Space used at {path} is :     {total_space//2**30 } GB {(total_space-(total_space//2**30)*2**30) //2**20} MB")
        elif(total_space>=2**20):
            print(f"Total Space used at {path} is :     {total_space//2**20} MB")
        else:
            print(f"Total space used at {path} is :     {total_space//2**10} KB")
        input("Press any key for more info : ")
        for file in fileinfo:
            if(file[1]>=2**30):
                print(f"Total Space used at {file[0]} is :      {file[1]//2**30 } GB {(file[1]-(file[1]//2**30)*2**30) //2**20} MB")
            elif(file[1]>=2**20):
                print(f"Total Space used at {file[0]} is :       {file[1]//2**20} MB {(file[1]-(file[1]//2**20)*2**20)//2**10} KB")
            else:
                print(f"Total Space used at {file[0]} is :        {file[1]//2**10} KB")
    elif(a==3):
        path=get_directory.get_directory()
        os.system("cls")
        walker=os.walk(path)
        res=[]
        rep={}
        rep=set(rep)
        for folder,subfolder,files in walker:
            for file in files:
                filepath=os.path.join(folder,file)
                sp=filepath.split('.')[-1]
                if(sp==filepath):
                    rep.add("File")
                else:    
                    rep.add(sp)
        for ele in rep:
            res.append([ele,0])
        walker=os.walk(path)
        for folder,subfolder,files in walker:
            for file in files:
                filepath=os.path.join(folder,file)
                coo=False
                sp=filepath.split('.')[-1]
                if(sp==filepath):
                    coo=True
                for ex in res:
                    if(coo):
                        if(ex=="File"):
                            ex[1]+=os.stat(filepath).st_size
                    if(filepath.endswith("."+ex[0])):
                        ex[1]+=os.stat(filepath).st_size
        for val in res:
            print("File Type : ",val[0],"Space used : " ,end="")
            if(val[1]>=2**30):
                print(f"{val[1]//2**30} GB {(val[1]-(val[1]//2**30)*2**30)//2**20} MB")
            elif(val[1]>=2**20):
                print(f"{val[1]//2**20} MB")
            else:
                print(f"{val[1]//2**10} KB")
    else:
        print("Wrong Choice")