# this is a refined version of the code.py python code

import os

# get the old and new directory fot the photos
Dir_Photos = input("Enter the path to the photos directory: ")
New_Dir_Photos = input("Now enter the new location for your organised photos: ")

fileList = os.listdir(Dir_Photos)

def IS_FILE(file):
    
    filePath = os.path.join(Dir_Photos, file)
    isFile = os.path.isfile(filePath)
    return isFile
    
for file in fileList:
    if IS_FILE(file):
        # do something