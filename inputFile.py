import os

DIRECTORY_NAME = ["mypt", "mypt2"]

def first_input():
    if not os.path.exists(DIRECTORY_NAME[0]):
        os.makedirs(DIRECTORY_NAME[0])
        fileNameLocation = DIRECTORY_NAME[0] + "/h.txt"
        testFile = open(fileNameLocation, "w+")
        testFile.write("H")
        testFile.close()
        return True
    else:
        print "Folder mypt Already Exists\n"
        return False

def second_input():
    fileNames = ["/h.txt", "/hello.txt", "/goobye.txt"]
    if not os.path.exists(DIRECTORY_NAME[1]):
        os.makedirs(DIRECTORY_NAME[1])
        fileNameLocation = DIRECTORY_NAME[1] + fileNames[0]
        testFile = open(fileNameLocation, "w+")
        testFile.write("H")
        testFile.close()
        fileNameLocation = DIRECTORY_NAME[1] + fileNames[1]
        testFile = open(fileNameLocation, "w+")
        testFile.write("Hello world")
        testFile.close()
        fileNameLocation = DIRECTORY_NAME[1] + fileNames[2]
        testFile = open(fileNameLocation, "w+")
        testFile.write("Good\nbye")
        testFile.close()
        return True
    else:
        print "Folder mypt2 Already Exists\n"
        return False
