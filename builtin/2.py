import string

def upper_lower(s):
    lower_alph = string.ascii_lowercase
    upper_alph = string.ascii_uppercase
    upper = 0
    lower = 0
    words = s.split(" ")
    for word in words:
        for letter in word:
            if letter in lower_alph:
                lower+=1
            elif letter in upper_alph:
                upper+=1
        
    
    return lower, upper

s = input()
print(upper_lower(s))
