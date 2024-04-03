import os

path = input()

def access_to_path(path):
    if os.path.exists():
        print('exists')
    else: 
        print('does not exists')

    if os.access(path, os.R_OK):
        print('readable')
    else:
        print('not readable')
    
    if os.access(path, os.W_OK):
        print('writeable')
    else:
        print('not writeable')
    
    if os.access(path, os.EX_OK):
        print('executable')
    else:
        print('not executable')

access_to_path(path)