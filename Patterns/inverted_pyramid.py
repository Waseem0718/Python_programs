def inverted_pyramid(row):
    
    for i in range(row,0,-1):
        for j in range(row-i):
            print("  ",end="")

        for k in range(2*i-1):
            print("* ",end="")

        print()

inverted_pyramid(5)