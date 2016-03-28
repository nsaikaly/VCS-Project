import os

g_a_DIRECTORY_NAME = ["mypt", "mypt2"]

def write_file(path, string):
    test_file = open(path, "w+")
    test_file.write(string)
    test_file.close()

def first_input():
    if not os.path.exists(g_a_DIRECTORY_NAME[0]):
        check_test(0)
        return True
    else:
        print "Folder mypt Already Exists\n"
        return False

def second_input():
    if not os.path.exists(g_a_DIRECTORY_NAME[1]):
        check_test(1)
        return True
    else:
        print "Folder mypt2 Already Exists\n"
        return False

def check_test(second):
    a_file_Names = ["/h.txt", "/hello.txt", "/goobye.txt"]
    os.makedirs(g_a_DIRECTORY_NAME[second])
    file_name_location = g_a_DIRECTORY_NAME[second] + a_file_Names[0]
    write_file(file_name_location, "H")

    if second == 1:
        file_name_location = g_a_DIRECTORY_NAME[second] + a_file_Names[1]
        write_file(file_name_location, "Hello world")
        file_name_location = g_a_DIRECTORY_NAME[second] + a_file_Names[2]
        write_file(file_name_location, "Good\nbye")