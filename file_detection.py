# Python file detection

import os

#file_path = "stuff/test.txt"           This is a text file which is located in stuff
file_path = "C:/Users/User/Desktop/Final"    # This is a local folder in my pc

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")


else:
    print("That location doesn't exist")