def reverse(s):
    words = []
    words = s.split(" ")
    reverse = words[::-1]
    reverse_sentence = " ".join(reverse)
    return reverse_sentence

s = input()
rev = reverse(s)
print(rev)
