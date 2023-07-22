import shutil

def space_availabe(path):
    return str(int(shutil.disk_usage(path)[2]// 2**30)) +" GB"

def space_used(path):
    return str(int(shutil.disk_usage(path)[1]//2**30)) +" GB"
