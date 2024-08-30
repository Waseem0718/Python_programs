def next_char(s):
    output = ""
    for i in range(len(s)):
        if i%2 == 0:
            output += s[i]
        else:
            output += chr(ord(s[i-1])+int(s[i]))

    return output

s = "a4k3b2"
print(next_char(s))

        