def roman_int(roman):
    roman_values = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    n = len(roman)
    total = 0
    for i in range(n):
        value = roman_values[roman[i]]
        if i < n-1 and roman_values[roman[i]] <  roman_values[roman[i+1]]:
            total -= value
            
        else:
            total += value

    return total

roman = "MCM"
print(roman_int(roman))

