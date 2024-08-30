n = 6
sum = 0
for i in range(1,n//2 + 1):
    if n%i ==0:
        sum += i

if sum == n:
    print("Perfect number")
else:
    print("not a perfect")

#