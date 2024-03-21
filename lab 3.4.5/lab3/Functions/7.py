def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True 
    return False


s = input()
x = s.split()
x = [int(i) for i in x]
print(has_33(x))
