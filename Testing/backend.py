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
        file_path = walk_tree()
        create_manifest(file_path)
        create_leaf(file_path)
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
    a_path_for_files = {}
    for (dirpath, dirnames, file_names) in os.walk(g_NAME_OF_REPO):
        if dirpath != g_NAME_OF_MANIFEST_FOLDER:
            a_list_of_files = []
            for file_name in file_names:
                a_list_of_files.append(file_name)
            a_path_for_files[dirpath] = a_list_of_files
    return a_path_for_files

# Creates the manifest file for the repo343 directory.
def create_manifest(directory_list):
    """Creates the manifest file for the repo343 directory.
    """
    MANIFEST = g_NAME_OF_MANIFEST_FOLDER + str(datetime.now())
    manifest_file = open(MANIFEST, 'w+')
    write_hierarchy(manifest_file, directory_list)
    manifest_file.close()

# Write the project tree to the manifest file.
def write_hierarchy(manifest_file, directory_list):
    """Write the project tree to the manifest file.
    """
    file_byte = 0L
    manifest_file.write("Project Tree Structure: \n")
    a_file_listing = write_file(manifest_file, directory_list)

    for file in a_file_listing:
        file_byte += os.stat(file).st_size

    manifest_file.write(str(len(a_file_listing)) + " Files\t" + str(file_byte) + " Bytes" + "\n")
    current_date = str(datetime.now().month) + "/" + str(datetime.now().day) + "/" + str(datetime.now().year)
    manifest_file.write(current_date)

def write_file(manifest_file, directory_list):
    a_file_listing = []
    for directory in directory_list:
        manifest_file.write("\t" + directory + "\n")
        for files in directory_list[directory]:
            a_file_listing.append(directory + "/" + files)
            manifest_file.write("\t\t" + directory + "/" + files + "/" + check_sum(directory + "/" + files) + "\n")
    return a_file_listing


# Creates the leaf directory folder for the files.
def create_leaf(directory_list):
    """Creates the leaf directory folder for the files.
    """
    for directory in directory_list:
        for files in directory_list[directory]:
            file_path = directory + "/"
            check_sum_name = check_sum(file_path + files)
            os.rename(file_path + files, file_path + check_sum_name)
            if not os.path.exists(file_path + files):
                os.makedirs(file_path + files)
            shutil.move(file_path + check_sum_name, file_path + files + "/" + check_sum_name)

# Gets the check_sum for the file.
def check_sum(file_name):
    """Gets the check_sum for the file.
    """
    file = open(file_name, 'r')
    check_sum = 0
    for line in file:
        for char in line:
            check_sum += ord(char)
    file.close()
    return str(check_sum)

# Uncomment line 103 if you are not running this script independently.
# create_repo()