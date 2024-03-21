def unique_elements(l):
    unique_list = []
    for item in l:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


l = []
s = input()
l = s.split(" ")
print(unique_elements(l))
