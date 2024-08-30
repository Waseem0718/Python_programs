def longest_word(str):
    punctuation = '''!@#$%^&*()_-+=[]{};:'"\|/`~,.?<>'''
    lt = []
    no_punc = ""
    for char in str:
        if char not in punctuation:
            no_punc += char

   
    word = ""
    for ch in no_punc:
        if ch == " ":
            lt.append(word)
            word=""
        else:
            word += ch

    if word:
        lt.append(word)
    
    return lt  
    
    
str = input()
print(longest_word(str))

