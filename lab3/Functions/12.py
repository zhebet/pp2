def histogram(l):
    for num in l:
        print('*' * num)

l = []
s = input()
l = s.split(" ")
l = [int(i) for i in l]
histogram(l)