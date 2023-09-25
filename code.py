import os

# path to the foto directory that will be organised
Dir_Poze ='/home/decebal/...../TESTING/'

# path to the organised photos
Dir_Poze_Final = '/home/decebal/..../TESTING/'

# save the list of images in given folder
filesList =os.listdir(Dir_Poze)

for file in filesList:

    # recreate the path to file
    filePath = os.path.join(Dir_Poze, file)

    # determine wether the file is or not a file
    isFile = os.path.isfile(filePath)
    
    if isFile:

        # determine the year when the image was created
        year =  file[0] + file[1] + file[2] + file[3] # this is a string

        Dir_year_path = os.path.join(Dir_Poze_Final, year)
        
        #create the folder if necessary
        try:
            os.mkdir(Dir_year_path)

        except:
            pass
        
            

        dst = os.path.join(Dir_year_path, file)

        os.replace(filePath, dst)
        # if yes then move file
        # else create and move file 
        # move image in directory year if it exists

    #print("File is a file: " + str(isFile)+ "\n")
