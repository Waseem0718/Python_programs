def rev_vowel(s):
    vowel = "aeiouAEIOU"
    char =[c for c in s if c in vowel]
    rev = char[::-1]
    index = 0
    result = []
    for ch in s:
        if ch in vowel:
            result.append(rev[index])
            index += 1
        else:
            result.append(ch)

    return ''.join(result)

s = "jaffer"
print(rev_vowel(s))