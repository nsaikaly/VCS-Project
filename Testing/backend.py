import os, shutil
from datetime import datetime

g_NAME_OF_REPO = "./repo343/"
g_NAME_OF_MANIFEST_FOLDER = "./repo343/MANIFEST/"


# Creates a repo343 that stores all the files for the project tree.
def create_repo():
    """Creates a repo343 that stores all the files for the project tree.
    """
    if not os.path.exists(g_NAME_OF_REPO):
        copy_tree();
        if not os.path.exists(g_NAME_OF_MANIFEST_FOLDER):
            os.makedirs(g_NAME_OF_MANIFEST_FOLDER)
        filePath = walk_tree()
        create_manifest(filePath)
        create_leaf(filePath)
        return True
    else:
        print g_NAME_OF_REPO + " Already Exists\n"
        return False

# Copies the project tree where backend.py is located.
def copy_tree():
    """Copies the project tree where backend.py is located.
    """
    FILES_TO_IGNORE = ('backend.py', 'backend.pyc', 'inputFile.py', 'inputFile.pyc', 'unitTest.py', 'unitTest.pyc', 'Testing', '.git', '*.md', '.DS_Store', '.gitignore', 'repo343', 'myptOutPut', 'mypt2OutPut', 'bothptOutPut')
    shutil.copytree(".", g_NAME_OF_REPO, ignore = shutil.ignore_patterns(*FILES_TO_IGNORE))

# Walk through the initial repo343 directory.
def walk_tree():
    """Walk through the initial repo343 directory.
    """
    pathForFiles = {}
    for (dirpath, dirnames, filenames) in os.walk(g_NAME_OF_REPO):
        if dirpath != g_NAME_OF_MANIFEST_FOLDER:
            alistOfFiles = []
            for filename in filenames:
                alistOfFiles.append(filename)
            pathForFiles[dirpath] = alistOfFiles
    return pathForFiles

# Creates the manifest file for the repo343 directory.
def create_manifest(directoryList):
    """Creates the manifest file for the repo343 directory.
    """
    MANIFEST = g_NAME_OF_MANIFEST_FOLDER + str(datetime.now())
    manifestFile = open(MANIFEST, 'w+')
    write_hierarchy(manifestFile, directoryList)
    manifestFile.close()

# Write the project tree to the manifest file.
def write_hierarchy(manifestFile, directoryList):
    """Write the project tree to the manifest file.
    """
    afileListing = []
    filebyte = 0L
    manifestFile.write("Project Tree Structure: \n")
    for directory in directoryList:
        directoryFiles = directoryList[directory]
        manifestFile.write("\t" + directory + "\n")
        for files in directoryFiles:
            filePath = directory + "/" + files
            checkSumName = check_sum(filePath)
            afileListing.append(filePath)
            manifestFile.write("\t\t" + filePath + "/" + checkSumName + "\n")
    for file in afileListing:
        fileInfo = os.stat(file)
        filebyte += fileInfo.st_size
    manifestFile.write(str(len(afileListing)) + " Files\t" + str(filebyte) + " Bytes" + "\n")
    date = datetime.now()
    currentDate = str(date.month) + "/" + str(date.day) + "/" + str(date.year)
    manifestFile.write(currentDate)

# Creates the leaf directory folder for the files.
def create_leaf(directoryList):
    """Creates the leaf directory folder for the files.
    """
    for directory in directoryList:
        directoryFiles = directoryList[directory]
        for files in directoryFiles:
            filePath = directory + "/"
            checkSumName = check_sum(filePath + files)
            os.rename(filePath + files, filePath + checkSumName)
            if not os.path.exists(filePath + files):
                os.makedirs(filePath + files)
            shutil.move(filePath + checkSumName, filePath + files + "/" + checkSumName)

# Gets the checksum for the file.
def check_sum(fileName):
    """Gets the checksum for the file.
    """
    file = open(fileName, 'r')
    checksum = 0
    for line in file:
        for char in line:
            checksum += ord(char)
    file.close()
    return str(checksum)

# Uncomment line 103 if you are not running this script independently.
# create_repo()