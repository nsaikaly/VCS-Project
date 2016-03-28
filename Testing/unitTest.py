import filecmp, shutil, os
from backend import create_repo
from inputFile import first_input, second_input

NAME_OF_MANIFEST_PATH = "./repo343/MANIFEST/"

def diffFile(manifestFile, outputFile):
    a_manifest = get_lines(manifestFile, [])
    a_output = get_lines(outputFile, [])
    for index in range(len(a_manifest) - 1):
        if a_manifest[index] != a_output[index]:
            return False
    return True

def get_lines(file, array):
    for line in file:
        array.append(line)
    return array

def get_manifest():
    for (dirpath, dirnames, filenames) in os.walk(NAME_OF_MANIFEST_PATH):
        return filenames[-1]

def first_test():
    assert first_input()
    assert create_repo()
    test_file("./myptOutPut")
    print "Removing mypt project tree and repo343 project tree"
    shutil.rmtree("mypt")
    shutil.rmtree("repo343")
    return True

def second_test():
    assert second_input()
    assert create_repo()
    test_file("./mypt2OutPut")
    print "Removing mypt project tree and repo343 project tree"
    shutil.rmtree("mypt2")
    shutil.rmtree("repo343")
    return True

def both_test():
    assert first_input()
    assert second_input()
    assert create_repo()
    test_file("./bothptOutput")
    print "Removing mypt and mypt2 project tree, and repo343 project tree"
    shutil.rmtree("mypt")
    shutil.rmtree("mypt2")
    shutil.rmtree("repo343")
    return True

def test_file(path):
    manifestFile = NAME_OF_MANIFEST_PATH + get_manifest()
    outputFile = open(path, "r")
    manifestFile = open(manifestFile, "r")
    assert diffFile(manifestFile, outputFile)
    print "Assert Successful. manifestFile equals " + path + "..."
    manifestFile.close()
    outputFile.close()

assert first_test()
assert second_test()
assert both_test()