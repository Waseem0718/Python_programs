def print_pattern(n):
    num = n * (n + 1) // 2  # Calculate the starting number
    for i in range(n):
        for j in range(i+1):
            print(format(num,"<3"),end=" ")
            num -= 1
        print()
# Example usage
n = 5
print_pattern(n)