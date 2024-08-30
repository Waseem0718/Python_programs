#longest subsequence btw same character
def long(str):
    maxi = 0
    l , r = 0,len(str)-1
    for i in range(len(str)):
        while True:
            if str[l] == str[r]:
                maxi = max(maxi,len(str[l+1:r]))
                break
            else:
                r -= 1
        l += 1
        r = len(str)-1
    
    return maxi

str = "cdddaadewojad"
print(long(str))


    