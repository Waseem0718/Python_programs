def uncommon_words(str1,str2):
    freq = {}
    for char in str1.split():
        freq[char] = freq.get(char,0)+1
    for char in str2.split():
        freq[char] = freq.get(char,0)+1

    lt = []
    for key,value in freq.items():
        if value == 1:
            lt.append(key)

    result = ' '.join(lt)
    return result

str1 = "he is very clever person"
str2 = "he is not a very clever person"
print(uncommon_words(str1,str2))
