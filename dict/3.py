import os
path=input()

def existence(path):
    if os.path.exists(path):
        for item in os.listdir(path):
            if os.path.isfile(os.path.join(path,item)):
                print(item)
            elif os.path.isdir(os.path.join(path, item)):
                print(item)

    else:
        print('does not exist') 
            