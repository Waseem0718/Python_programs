def sortbyfreq(str):
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] = char_count.get(char , 0) + 1
        else:
            char_count[char] = 1
    
    print(char_count)
    sorted_char = sorted(char_count.items(),key = lambda x : x[1], reverse=True)
    print(sorted_char)
    result = "".join(char * freq for char, freq in sorted_char)

    return result

str = "jaffer"
print(sortbyfreq(str))