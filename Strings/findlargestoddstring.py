def largestoddnumber(str):
    ans= ""
    for i in range(len(str)-1,0,-1):
        if int(str[i]) % 2 != 0:
            return str[:i+1]
        
str = "982798667212"
print(largestoddnumber(str))
