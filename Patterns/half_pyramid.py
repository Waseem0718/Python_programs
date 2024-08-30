def half_pyramid(row):

    for i in range(0,row):
        for j in range(i+1):
            print("* ",end="")
        print()

half_pyramid(5)