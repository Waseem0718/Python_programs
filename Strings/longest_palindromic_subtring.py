def longest_palindromic_substring(s):
    longest = ""
    for i in range(len(s)):
        r = len(s)-1
        while i<= r:
           if s[i:r+1] == s[i:r+1][::-1]:
               if len(s[i:r+1]) > len(longest):
                   longest += s[i+r+1]
           else:
               r -= 1

    return longest

s = "abadc"
print(longest_palindromic_substring(s))