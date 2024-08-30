def leap_year(year):
    if year % 4  == 0 and (year % 400 == 0 or year % 100 != 0 ):
        return "Leap year"
    else:
        return "Not a Leap year"
    
print(leap_year(2024))