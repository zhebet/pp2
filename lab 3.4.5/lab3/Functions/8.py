def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

s = input()
list = s.split()
list = [int(item) for item in list]
print(spy_game(list))
