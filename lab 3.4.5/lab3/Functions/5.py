def permutations(input_str):
    if len(input_str) <= 1:
        return [input_str]

    perms = []

    for i, char in enumerate(input_str):
        remaining_chars = input_str[:i] + input_str[i+1:]
        
        for perm in permutations(remaining_chars):
            perms.append(char + perm)

    return perms


s = input()
perms = permutations(s)
for perm in perms:
    print(perm)

