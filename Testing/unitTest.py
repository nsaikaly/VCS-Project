import filecmp, shutil, os
from backend import create_repo
from inputFile import first_input, second_input

NAME_OF_MANIFEST_PATH = "./repo343/MANIFEST/"

def diff_file(manifest_file, output_file):
    a_manifest = get_lines(manifest_file, [])
    a_output = get_lines(output_file, [])
    for index in range(len(a_manifest) - 1):
        if a_manifest[index] != a_output[index]:
            return False
    return True

def get_lines(file, array):
    for line in file:
        array.append(line)
    return array

def get_manifest():
    for (dir_path, dir_names, file_names) in os.walk(NAME_OF_MANIFEST_PATH):
        return file_names[-1]

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
    manifest_file = NAME_OF_MANIFEST_PATH + get_manifest()
    output_file = open(path, "r")
    manifest_file = open(manifest_file, "r")
    assert diff_file(manifest_file, output_file)
    print "Assert Successful. manifest_file equals " + path + "..."
    manifest_file.close()
    output_file.close()

assert first_test()
assert second_test()
assert both_test()