import os

# List of Directory name for sample input directories.
g_a_DIRECTORY_NAME = ["mypt", "mypt2"]

# Write the string to a given file path.
# Global: None.
# ALine Count = 3
def write_file(path, string):
    """Write the string to a given file path."""

    test_file = open(path, "w+") # open file from a given path.

    test_file.write(string) # write the string to the file.

    test_file.close() # Close the file.

# Test the first Input.
# Global: g_a_DIRECTORY_NAME list to check if a given path exists.
# ALine Count = 4
def first_input():
    """Test the first Input."""

    # check if a given g_a_DIRECTORY_NAME path exist.
    if not os.path.exists(g_a_DIRECTORY_NAME[0]):
        create_directory(0) # Create directory with parameter 0

        create_file(0) # Create file with parameter 0

        return True # Return True for assert purpose.

    else:
        print "Folder mypt Already Exists"

        return False # Return False for assert purpose.

# Test the second Input.
# Global: g_a_DIRECTORY_NAME list to check if a given path exists.
# ALine Count = 4
def second_input():
    """Test the second Input."""

    # check if a given g_a_DIRECTORY_NAME path exist.
    if not os.path.exists(g_a_DIRECTORY_NAME[1]):
        create_directory(1) # Create directory with parameter 1

        create_file(1) # Create file with parameter 1

        return True # Return True for assert purpose.

    else:
        print "Folder mypt2 Already Exists"

        return False # Return False for assert purpose.

# Create test directory for input files.
# Global: g_a_DIRECTORY_NAME list to create a directory.
# ALine Count = 1
def create_directory(second):
    """Create test directory for input files."""

    # Create directory of a given list path.
    os.makedirs(g_a_DIRECTORY_NAME[second])

# Create test sample for input files.
# Global: g_a_DIRECTORY_NAME list to create a file at a given path.
# ALine Count = 8
def create_file(second):
    """Create test sample for input files."""

    # List of file names.
    a_file_Names = ["/h.txt", "/hello.txt", "/goobye.txt"]

    # file name path for the file name.
    file_name_location = g_a_DIRECTORY_NAME[second] + a_file_Names[0]

    # Wirte to file.
    write_file(file_name_location, "H")

    # Check for second
    if second == 1:

        # file name path for the file name
        file_name_location = g_a_DIRECTORY_NAME[second] + a_file_Names[1]

        # Wirte to file.
        write_file(file_name_location, "Hello world")

        # file name path for the file name
        file_name_location = g_a_DIRECTORY_NAME[second] + a_file_Names[2]

        # Wirte to file.
        write_file(file_name_location, "Good\nbye")