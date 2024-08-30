def substring_in_string(str1,str2):

    if str2 in str1:
        return str1.index(str2[0])
    else:
        return -1
    
str1 = "text123book"
str2 = "123"
print(substring_in_string(str1,str2))

    


