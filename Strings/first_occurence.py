def first_occurence(str1,str2):
    lt = []
    for i in range(0,len(str2)):
        for j in range(0,len(str1)):
            if str2[i] == str1[j]:
                lt.append(j)
                break

    lt.sort()
    return str1[lt[0]:lt[-1]+1]

   

str1 = "WASEEMULLAH"
str2 = "SAL"
print(first_occurence(str1,str2))
            