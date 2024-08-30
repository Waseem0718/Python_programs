def remove_consecutive(s):
    result = ""
    for ch in s:
        if ch not in result:
            result += ch

    return result

s = "aabbccddeeff"
print(remove_consecutive(s))
