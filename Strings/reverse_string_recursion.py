def revrerse_words(s):
    result = []
    words = ""
    for ch in s:
        if ch == " ":
            result.append(words)
            words = ""
        else:
            words += ch

    if words:
        result.append(words)

    return ' '.join(recursive_reverse(result))

def recursive_reverse(result):

    if len(result) <= 1:
        return result

    return recursive_reverse(result[1:]) + [result[0]]            

    

s = "one two three"
print(revrerse_words(s))