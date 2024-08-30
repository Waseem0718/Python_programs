def palindrome(n):
    digit = 0
    mod= 0
    temp = n
    while temp > 0:
        mod = temp % 10
        digit = (digit * 10) + mod
        temp = temp//10

    if digit == n:
        return "Palindrome"
    else:
        return "Not a palindrome"
    
print(palindrome(151151))



    
