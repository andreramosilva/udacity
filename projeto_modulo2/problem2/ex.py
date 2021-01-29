## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os


# Let us print the files in the directory in which you are running this script
# print (os.listdir("."))

# Let us check if this file is indeed a file!
# print (os.path.isfile("./ex.py"))

# Does the file end with .py?
# print ("./ex.py".endswith(".py"))

def check_dir(path):
    if os.path.isdir(path):
        return True
    else:
        return False
    # return paths


def find_sub_folders(path):
    return os.listdir(path)


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # print(path)
    # print (os.listdir(path))

    paths = [path]

    if check_dir(path):
        paths.append(path)
        sub_folders = find_sub_folders(path)
        for index in range(len(sub_folders)):
            print(sub_folders[index])
            if check_dir(sub_folders[index]):
                print(sub_folders[index], True)
            # sub_sub_folder = find_sub_folders(folder)
            # for item in sub_sub_folder:
            #	print(item)


print(find_files('*', './testdir'))
