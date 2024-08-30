def merge_string_alternatively(str1,str2):
    str3 = ""
    for i in range(0,max(len(str1),len(str2))):
            str3 += str1[i]
            str3 += str2[i]

    return str3

str1 = "waseem"
str2 = "jaffer"
print(merge_string_alternatively(str1,str2))