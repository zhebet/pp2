nums = []
s = input()
nums = s.split(" ")
nums = [int(i) for i in nums]

prime_nums = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) if x > 1 else False, nums))
print("Prime numbers:", prime_nums)
