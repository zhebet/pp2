def palindrome(s):
    words = s.split(" ")
    return s == s[::-1]

s = input()
if palindrome(s):
    print("yes")
else:
    print("No")
