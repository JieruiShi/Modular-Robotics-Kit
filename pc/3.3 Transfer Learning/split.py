import os
import numpy as np
import shutil

sourceRoot = 'flowers'
outputRoot = 'flowers-split'


classes = os.listdir(sourceRoot) # Get all the classes

for i in classes:
    
    os.makedirs(outputRoot + '/train/' + i) # Create train, test, valid directories
    os.makedirs(outputRoot + '/test/' + i)
    os.makedirs(outputRoot + '/valid/' + i)

    train_ratio = 0.7
    test_ratio = 0.2

    allFileNames = os.listdir(sourceRoot + '/' + i) #List all file names under the directory
    np.random.shuffle(allFileNames) #Shuffles the list

    train_FileNames, test_FileNames, valid_FileNames = np.split(np.array(allFileNames),
    [int(len(allFileNames)*train_ratio),int(len(allFileNames)*(test_ratio + train_ratio))])
    #Splits the List to train, test and valid file lists

    train_FileNames = [sourceRoot + i + '/'+ name for name in train_FileNames.tolist()]
    test_FileNames = [sourceRoot + i + '/' + name for name in test_FileNames.tolist()]
    valid_FileNames = [sourceRoot + i + '/' + name for name in valid_FileNames.tolist()]
    

    for name in train_FileNames:
        shutil.copy(name, outputRoot +'/train/' + i)

    for name in test_FileNames:
        shutil.copy(name, outputRoot +'/test/' + i)
      
    for name in valid_FileNames:
        shutil.copy(name, outputRoot +'/valid/' + i)