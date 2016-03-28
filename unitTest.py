import inputFile, backend, filecmp, shutil, os
from backend import create_repo
from inputFile import first_input, second_input

NAME_OF_MANIFEST_PATH = "./repo343/MANIFEST/"

def diffFile(manifestFile, outputFile):
    manifest = getLines(manifestFile, [])
    output = getLines(outputFile, [])
    for index in range(len(manifest) - 1):
        if manifest[index] != output[index]:
            return False
    return True

def getLines(file, array):
    for line in file:
        array.append(line)
    return array

def getManifestFile():
    for (dirpath, dirnames, filenames) in os.walk(NAME_OF_MANIFEST_PATH):
        return filenames[-1]

def firstUnitTest():
    if not first_input():
        return False
    if not create_repo():
        return False
    manifestFile = NAME_OF_MANIFEST_PATH + getManifestFile()
    outputFile = open("./myptOutPut", "r")
    manifestFile = open(manifestFile, "r")
    if not diffFile(manifestFile, outputFile):
        return False
    print "Assert Successful. manifestFile equals myptOutput...\n"
    manifestFile.close()
    outputFile.close()
    print "Removing mypt project tree and repo343 project tree"
    shutil.rmtree("mypt")
    shutil.rmtree("repo343")

def secondUnitTest():
    if not second_input():
        return False
    if not create_repo():
        return False
    manifestFile = NAME_OF_MANIFEST_PATH + getManifestFile()
    outputFile = open("./mypt2OutPut", "r")
    manifestFile = open(manifestFile, "r")
    if not diffFile(manifestFile, outputFile):
        return False
    print "Assert Successful. manifestFile equals mypt2Output...\n"
    manifestFile.close()
    outputFile.close()
    print "Removing mypt project tree and repo343 project tree"
    shutil.rmtree("mypt2")
    shutil.rmtree("repo343")
    return True

def bothUnitTest():
    if not first_input():
        return False
    if not second_input():
        return False
    if not create_repo():
        return False
    manifestFile = NAME_OF_MANIFEST_PATH + getManifestFile()
    outputFile = open("./bothptOutput", "r")
    manifestFile = open(manifestFile, "r")
    if not diffFile(manifestFile, outputFile):
        return False
    print "Assert Successful. manifestFile equals bothptOutput...\n"
    manifestFile.close()
    outputFile.close()
    print "Removing mypt and mypt2 project tree, and repo343 project tree"
    shutil.rmtree("mypt")
    shutil.rmtree("mypt2")
    shutil.rmtree("repo343")
    return True

assert first_input()
assert second_input()
assert bothUnitTest()