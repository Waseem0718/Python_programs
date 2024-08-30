def vowel_cons(str1):
    vowel = "AEIOUaeiou"
    count_of_vowel = 0
    count_of_cons = 0

    for ch in str1:
        if ch in vowel:
            count_of_vowel += 1
        else:
            count_of_cons += 1

    return count_of_vowel, count_of_cons

str1 = "waseemullah"

print(vowel_cons(str1))
