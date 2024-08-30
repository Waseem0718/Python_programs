def missingnum(num,n):
    temp = n * (n + 1) // 2
    sum = 0
    for i in num:
        sum += i

    missing  = temp - sum
    return missing

n = 5
num = map(int, input().split())
print(missingnum(num,n))