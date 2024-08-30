def hollow_pyramid(row):

    for i in range(row):
        for j in range(row):
            if j == 0 or j == i or i == (row-1):
                print("* ",end='')
            else:
                print(end="  ")
        print()

row = 5
hollow_pyramid(row)