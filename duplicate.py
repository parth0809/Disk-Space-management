import hashlib  
import os 


# walker walk in directory and generate a path of folder,subfolder,files


def find_duplicates(path):
    walker=os.walk(path)
    unique_file=dict()
    duplicates=dict()
    for folder,subfolder,files in walker:
        for file in files:
            filepath=os.path.join(folder,file)
            filehash=hashlib.md5(open(filepath,"rb").read()).hexdigest()
            if(filehash in unique_file.keys()):
                duplicates[filehash].append(filepath)
            else:
                unique_file[filehash]=filepath
                duplicates[filehash]=[]

    return unique_file,duplicates

def find_duplicates_of_file(path,filepth):
    hash=hashlib.md5(open(filepth,"rb").read()).hexdigest()
    walker=os.walk(path)
    duplicates=[]
    for folder,subfolder,files in walker:
        for file in files:
            filepath=os.path.join(folder,file)
            filepath=filepath.replace('\\','/')
            filehash=hashlib.md5(open(filepath,"rb").read()).hexdigest()
            if(not(filepath == filepth)):

                if(filehash==hash):
                    duplicates.append(filepath)
    return duplicates

