def remove_palindrome(str):
    result = []
    for char in str:
        rev = char[::-1]
        if rev != char:
            result.append(char)
        
    return " ".join(result)

str = "he speak malayalam".split()
print(remove_palindrome(str))