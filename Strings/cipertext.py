def ceaserciper(s):
    result = []
    for char in s:
        if 'a'<= char <= 'z':
            rem = ord(char) - ord("a")
            dec = (rem + 3) % 26
            dec_char = chr(dec + ord('a'))
            result.append(dec_char)
        

    return ''.join(result)

s = "abcde"
print(ceaserciper(s))