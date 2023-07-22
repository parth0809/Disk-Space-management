import os

def large_files(path):
    sol=[]
    walker=os.walk(path)
    print("What you consider large file.? ")
    gb=int(input("GB : "))
    mb=int(input("MB :"))
    kb=int(input("KB :"))
    mb=mb+kb/2**10
    kb=kb%2**10
    gb=gb+mb/2**10
    mb=mb%2**10
    large=gb*2**30+mb*2**20+kb*2**10
    for folder,subfolder,files in walker:
        for file in files:
            filepath=os.path.join(folder,file)
            if((os.stat(filepath).st_size)//large >=1):
                sol.append([filepath,os.stat(filepath).st_size])
    return sol

