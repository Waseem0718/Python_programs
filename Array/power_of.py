def check_power(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1

n = 1024
if check_power(n):
    print(f"{n} is power of 2")
else:
    print(f"{n} is not a power of 2")
 