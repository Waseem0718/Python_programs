# def uppertolower(str1):
   
#     result = ""
#     for ch in str1:
#        if 'A'<= ch <= 'Z':
#           result += chr(ord(ch)+32)

#     return result

# str1 = "ERHEW"
# print(uppertolower(str1))

def lowertoupper(str2):
   
    result = ""
    for ch in str2:
        if 'a'<= ch <= 'z':
            result += chr(ord(ch)-32)

    return result

str2 = "tytf"
print(lowertoupper(str2))
