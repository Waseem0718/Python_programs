def full_pyramid(row):

    for i in range(row):
        for j in range(row-i+1):
            print("  ",end="")
    

        for k in range(2*i+1):
            print("* ",end="")
        print()
    

full_pyramid(5)