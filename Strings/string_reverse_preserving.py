def reverse(s):
    alphanum = "abcderfghijklmnopqrstuvwzyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"    
    char = [c for c in s if c in alphanum]
    rev = char[::-1]
    result = []
    index = 0
    for c in s:
        if c in alphanum:
            result.append(rev[index])
            index += 1
        else:
            result.append(c)

    return ''.join(result)

s = "house no : 123@ abc"
print(reverse(s))