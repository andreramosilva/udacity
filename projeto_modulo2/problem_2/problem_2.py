## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))


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
    list_of_paths = []
    if suffix == "*":

        if not os.path.isdir(path):
            list_of_paths.append(path)
            return list_of_paths
        else:
            current_path = os.listdir(path)
            for sub_path in current_path:
                current_sub_path = os.path.join(path, sub_path)

                list_of_paths.append(current_sub_path)
                list_of_paths.append(find_files("*", current_sub_path))

            return  list_of_paths       #print(list_of_paths)
    else:
        #list_of_paths = []
        if not os.path.isdir(path):
            if path.endswith(suffix):
                list_of_paths.append(path)
                return list_of_paths
        else:
            current_path = os.listdir(path)
            for sub_path in current_path:
                current_sub_path = os.path.join(path, sub_path)
                if current_sub_path.endswith(suffix):
                    list_of_paths.append(current_sub_path)
                list_of_paths.append(find_files(suffix, current_sub_path))
                #print(list_of_paths)


            return list_of_paths

print(find_files( ".h", "."))

