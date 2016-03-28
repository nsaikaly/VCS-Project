import filecmp, shutil, os
from backend import create_repo
from inputFile import first_input, second_input

g_NAME_OF_MANIFEST_PATH = "./repo343/MANIFEST/"

# Find the Difference in every line for file.
# Globals: None.
# ALine Count = 6
def diff_file(manifest_file, output_file):
    """Find the Difference in every line for file."""

    # List of lines for manifest file.
    a_manifest = get_lines(manifest_file, [])

    # List of lines for the sample output file.
    a_output = get_lines(output_file, [])

    # Loop through length of the manifest file size - 1.
    for index in range(len(a_manifest) - 1):

        # Check if the lines are identical.
        if a_manifest[index] != a_output[index]:
            return False # Return false for Assert Purpose.

    return True # Return True for Assert Purpose.

# Gets every line for a file.
# Globals: None.
# ALine Count = 3
def get_lines(file, array):
    """Gets every line for a file."""

    # Loop through the file and get the lines.
    for line in file:
        array.append(line) # Append the lines to the array.

    return array # Return the array.

# Gets the most recent Manifest File.
# Globals: g_NAME_OF_MANIFEST_PATH as parameter to walk in a path.
# ALine Count = 2
def get_manifest():
    """Gets the most recent Manifest File."""

    # walk through the directory for the g_NAME_OF_MANIFEST_PATH path
    for (dir_path, dir_names, file_names) in os.walk(g_NAME_OF_MANIFEST_PATH):
        return file_names[-1] # return the most recent manifest file

# First Unit Test on a minimal ptree and file.
# Globals: None.
# ALine Count = 6
def first_test():
    """First Unit Test on a minimal ptree and file."""

    # assert first_input function.
    assert first_input()

    # assert create_repo function.
    assert create_repo()

    # test file for sample output.
    test_file("./myptOutPut")

    print "Removing mypt project tree and repo343 project tree"

    # remove the mypt project tree.
    shutil.rmtree("mypt")

    # remove the repo343 project tree.
    shutil.rmtree("repo343")

    return True # return True for assert purpose.

# Second Unit Test Input on a tiny ptree with files.
# Globals: None.
# ALine Count = 6
def second_test():
    """Second Unit Test Input on a tiny ptree with files."""

    # assert second_input function.
    assert second_input()

    # assert create_repo function.
    assert create_repo()

    # test file for sample output.
    test_file("./mypt2OutPut")

    print "Removing mypt project tree and repo343 project tree"

    # remove the mypt project tree.
    shutil.rmtree("mypt2")

    # remove the repo343 project tree.
    shutil.rmtree("repo343")

    return True # return True for assert purpose.

# Third Unit Test Input on both minimal ptree and file, and on a tiny ptree with files.
# Globals: None.
# ALine Count = 7
def both_test():
    """Third Unit Test Input on both minimal ptree and file, and on a tiny ptree with files."""

    # assert first_input function
    assert first_input()

    # assert second_input function
    assert second_input()

    # assert create_repo function
    assert create_repo()

    # test file for sample output.
    test_file("./bothptOutput")

    print "Removing mypt and mypt2 project tree, and repo343 project tree"

    # remove mypt project tree.
    shutil.rmtree("mypt")

    # remove mypt2 project tree.
    shutil.rmtree("mypt2")

    # remove repo343 project tree.
    shutil.rmtree("repo343")

    return True # return True for assert purpose.

# Check the output file and the manifest file.
# Globals: g_NAME_OF_MANIFEST_PATH to get the path for the manifest file
# ALine Count = 6
def test_file(path):
    """Check the output file and the manifest file."""

    # set manifest file path
    manifest_file = g_NAME_OF_MANIFEST_PATH + get_manifest()

    # open the sample output path
    output_file = open(path, "r")

    # open the manifest output path
    manifest_file = open(manifest_file, "r")

    # assert diff_file function with the two open files
    assert diff_file(manifest_file, output_file)

    print "Assert Successful. manifest_file equals " + path + "..."

    manifest_file.close() # Close file

    output_file.close() # Close file

assert first_test() # Call first_test function

assert second_test() # Call second_test function

assert both_test() # Call both_test function