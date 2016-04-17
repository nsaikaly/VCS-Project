from create_repo import check_sum
from datetime import datetime
import create_repo
import os, shutil

g_NAME_OF_CURRENT_DIRECTORY = os.getcwd()
g_NAME_OF_REPO = g_NAME_OF_CURRENT_DIRECTORY + "/repo343" # Repo Directory Path.
g_NAME_OF_MANIFEST_FOLDER = g_NAME_OF_CURRENT_DIRECTORY + "/repo343/MANIFEST" # Manifest Directory Path.
g_DIRECTORY_AND_FILES_TO_IGNORE = set([".git", "repo343", "check_in.py", "check_out.py", "create_repo.py", "create_repo.pyc", "Testing", "README.md", ".gitignore", "check_in.pyc", "check_out.pyc"])

def check_in():
    file_path = walk_directory()
    check_directory(file_path)
    create_manifest(file_path)
    pass

def walk_directory():
    a_path_for_files = {}
    for (dir_path, dir_name, file_names) in os.walk(g_NAME_OF_CURRENT_DIRECTORY, topdown = True):
        dir_name[:] = [d for d in dir_name if d not in g_DIRECTORY_AND_FILES_TO_IGNORE]
        file_names[:] = [f for f in file_names if f not in g_DIRECTORY_AND_FILES_TO_IGNORE]
        list_of_files = []
        for file_name in file_names:
            list_of_files.append(file_name)
        a_path_for_files[dir_path] = list_of_files
    return a_path_for_files

def check_directory(file_path):
    for files in file_path:
        for file in file_path[files]:
            directoryPath = g_NAME_OF_REPO + "/" + file
            checkSumName = check_sum(files + "/" + file)
            if not os.path.isdir(directoryPath):
                os.makedirs(directoryPath)
            if not os.path.exists(directoryPath + "/" + checkSumName):
                shutil.copyfile(files + "/" + file, directoryPath + "/" + checkSumName)

# Creates the manifest file for the repo343 directory.
# Globals: g_NAME_OF_MANIFEST_FOLDER use for file path.
# ALine count = 4
def create_manifest(directory_list):
    """Creates the manifest file for the repo343 directory."""

    # Sets the file name of MANIFEST to the current datetime.
    MANIFEST = g_NAME_OF_MANIFEST_FOLDER + "/" + str(datetime.now())

    # Create and open manifest file.
    manifest_file = open(MANIFEST, 'w+')

    # Write project tree hierachy to manifest file.
    write_hierarchy(manifest_file, directory_list)

    # Writes the parent file to the manifest
    write_parent(manifest_file)

    # Close manifest file.
    manifest_file.close()

def write_parent(manifest_file):
    manfile = []
    for (dir_path, dir_name, file_names) in os.walk(g_NAME_OF_MANIFEST_FOLDER):
        manfile = file_names
    manfile.sort()
    manifest_file.write("\nParent file: " + str(manfile[-1]))

# Write the project tree to the manifest file.
# Globals: None.
# ALine count = 7
def write_hierarchy(manifest_file, directory_list):
    """Writes the project hierarchy to the manifest file."""

    file_byte = 0L # Variable to get total byte size of files.

    # Write to file and get the path for all the files.
    a_file_listing = write_file(manifest_file, directory_list)

    # Get total byte size for every files.
    for file in a_file_listing:
        file_byte += os.stat(file).st_size

    # Write the number of files and the total size of files.
    manifest_file.write(str(len(a_file_listing)) + " Files\t" + str(file_byte) + " Bytes" + "\n")

    # sets the current_date to todays month/day/year respectively.
    current_date = str(datetime.now().month) + "/" + str(datetime.now().day) + "/" + str(datetime.now().year)

    # Write the current date to the file.
    manifest_file.write(current_date)

# Helper function for write_hierarchy.
# Globals: None.
# ALine count = 9
def write_file(manifest_file, directory_list):
    """Helper function for write_hierarchy."""

    a_file_listing = [] # Array to hold all file path.

    manifest_file.write("Project Tree Structure: \n") # Write string to file

    # loop through the directory in the list of directories
    manifest_file.write("\t" + g_NAME_OF_REPO + "\n")

    for directory in directory_list:

        for file in directory_list[directory]:
            manifest_file.write("\t\t" + g_NAME_OF_REPO + "/" + file + "/" + check_sum(directory + "/" + file)+ "\n")

            # Append path for files to listing
            a_file_listing.append(g_NAME_OF_REPO + "/" + file + "/" + check_sum(directory + "/" + file))

                # Append path for files to listing
                # a_file_listing.append(directory_list[directory])

    return a_file_listing # return list of file paths.


if __name__ == "__main__":
    check_in()