def max_freq_char(str1):
    freq = {}
    for char in str1:
        if char in freq:
            freq[char] = freq.get(char,0)+1
        else:
            freq[char] = 1
    sorted_freq = dict(sorted(freq.items(),key = lambda x : x[1]))

    val = list(sorted_freq.values())[-1]
    for key,value in freq.items():
        if val == value:
            return key

    
str1 = "programming"
print(max_freq_char(str1))