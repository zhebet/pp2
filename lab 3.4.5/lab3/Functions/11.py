def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


word = input()
if is_palindrome(word):
    print("Palindrome!")
else:
    print("Not a palindrome.")

