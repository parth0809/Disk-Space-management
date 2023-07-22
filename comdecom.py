import zipfile 

def compress(path):
    replace_file=path.split('.')[0]+ ".zip"
    replace_file=replace_file.replace('\\','/')
    with zipfile.ZipFile(replace_file,'w') as zipfiles:
        zipfiles.write(path,compress_type=zipfile.ZIP_DEFLATED)

def decompress(path):
    ls=path.split('/')
    pth=""
    for i in range(len(ls)-1):
        pth+=ls[i]+'\\'
    pth=pth[: -1]
    with zipfile.ZipFile(path,'r') as zipfiles:
        zipfiles.extractall(pth)