path = input()
line = input().split(" ")
file = open("path", 'w')

for item in line:
    file.write(item)
