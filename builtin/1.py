def mult_list(numbers):
    res = 1
    for num in numbers:
        res *= num
    return res

s = input().split(' ')
n = [int(i) for i in s]
print(mult_list(n))