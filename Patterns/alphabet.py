def alphabet_pattern(n):
    alpha = 65
    for i in range(0,n):
        for j in range(i+1):
            print(chr(alpha+j),end=" ")
        alpha += 1
        print()

alphabet_pattern(5)