# def checkrotatestring(s,g):
#     temp = ""
#     for i in range(0,len(s)):
#         temp = s[i:] + s[:i]
#         if temp == g:
#             return True
        
#     return False

# s = "abcde"
# g = "cbdea"
# print(checkrotatestring(s,g))

def rotate(str1, k):
    n = len(str1)
    k = k % n
    r = str1[-k:] + str1[:-k]

    return r

str1 = "abcde"
k = 2
print(rotate(str1,k))