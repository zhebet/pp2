import os
path = input()

def path_dict_files(path):
    print("Directories:")
    for item in os.listdir():
        if os.path.isdir(os.path.join(path, item)):
            print(item)
    
    print("\nFiles:")
    for item in os.listdir():
        if os.path.isfile(os.path.join(path,item)):
            print(item)
    
    print("\nAll Directories and Files")
    for item in os.listdir():
        if os.path.isfile(os.path.join(path,item)):
            print(item)
        if os.path.isdir(os.path.join(path, item)):
            print(item)

path_dict_files(path)
