import os
path = input()

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
    