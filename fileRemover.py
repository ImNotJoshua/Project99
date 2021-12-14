from _typeshed import FileDescriptor
import os
import shutil
import time

def main():
    path=input("Enter the files you want to remove:")
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root_folders, folders, files in os.walk(path):
            if seconds >= getFolderAge(root_folders):
                removeFolder(root_folders)
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(root_folders, folder)
                    if seconds > getFolderAge(folder_path):
                        removeFolder(folder_path)
                for file in files:
                    file_path=os.path.join(root_folders, file)
                    if seconds > getFolderAge(file_path):
                        removeFiles(file_path)

    else:
        print("The file path does not exist")

def getFolderAge(path):
    ctime=os.stat(path).st_ctime
    return ctime

def removeFolder(path):
    if not shutil.rmtree(path):
        print("Path has been removed succesfully")
    else:
        print("We are unable to delete the path")

def removeFiles(path):
    if not os.remove(path):
        print("file has been removrd succesfully")
    else:
            print("We are unable to remove the file")
    
