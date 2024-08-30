def armstrong(n):
    digit  = 0
    alter = n
    while alter:
        temp = alter % 10
        digit = digit + temp**len(str(n))
        alter = alter//10

    return digit

n = 407
result = armstrong(n)
if n == result:
    print("Armstrong number")
else:
    print("Not an armstrong number")