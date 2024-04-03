def all_true(t):
    return all(t)

s = input()
w = s.split()
t = tuple(eval(i) for i in w)
print(all_true(t))