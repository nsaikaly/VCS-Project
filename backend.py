import os, shutil
from datetime import datetime

NAME_OF_REPO = "./repo343"
NAME_OF_MANIFEST_FOLDER = "./repo343/MANIFEST"
FILES_TO_IGNORE = ('*.pyc', '*.py', 'venv', '.git', '*.md', '.DS_Store', '.gitignore', 'repo343')

def createRepo():
    copyProjectTree();

    if not os.path.exists(NAME_OF_MANIFEST_FOLDER):
        os.makedirs(NAME_OF_MANIFEST_FOLDER)
    filePath = walkThroughProjectTree()
    createManifest(filePath)
    createLeafFoler(filePath)

def copyProjectTree():
    shutil.copytree(".", NAME_OF_REPO, ignore = shutil.ignore_patterns(*FILES_TO_IGNORE))

def walkThroughProjectTree():
    pathForFiles = {}
    for (dirpath, dirnames, filenames) in os.walk(NAME_OF_REPO):
        if dirpath != NAME_OF_MANIFEST_FOLDER:
            listOfFiles = []
            for filename in filenames:
                listOfFiles.append(filename)
            pathForFiles[dirpath] = listOfFiles
    return pathForFiles

def createManifest(directoryList):
    MANIFEST = NAME_OF_MANIFEST_FOLDER + "/" + str(datetime.now())
    manifestFile = open(MANIFEST, 'w+')
    writeProjectHierarchy(manifestFile, directoryList)

def writeProjectHierarchy(manifestFile, directoryList):
    fileListing = []
    filebyte = 0L
    manifestFile.write("Project Tree Structure: \n")
    for directory in directoryList:
        directoryFiles = directoryList[directory]
        manifestFile.write("\t" + directory + "\n")
        for files in directoryFiles:
            filePath = directory + "/" + files
            checkSumName = getCheckSum(filePath)
            fileListing.append(filePath)
            manifestFile.write("\t\t" + filePath + "/" + checkSumName + "\n")
    for file in fileListing:
        fileInfo = os.stat(file)
        filebyte += fileInfo.st_size
    manifestFile.write(str(len(fileListing)) + " Files\t" + str(filebyte) + " Bytes" + "\n")
    date = datetime.now()
    currentDate = str(date.month) + "/" + str(date.day) + "/" + str(date.year)
    manifestFile.write(currentDate)

def createLeafFoler(directoryList):
    for directory in directoryList:
        directoryFiles = directoryList[directory]
        for files in directoryFiles:
            filePath = directory + "/"
            checkSumName = getCheckSum(filePath + files)
            os.rename(filePath + files, filePath + checkSumName)
            if not os.path.exists(filePath + files):
                os.makedirs(filePath + files)
            shutil.move(filePath + checkSumName, filePath + files + "/" + checkSumName)

def getCheckSum(fileName):
    file = open(fileName, 'r')
    checksum = 0
    for line in file:
        for char in line:
            checksum += ord(char)
    return str(checksum)

createRepo();