def diamond(r):
    #pryramid
    for i in range(0,r):
        for j in range(r-i-1):
            print(" ",end=" ")
        for k in range(2*i+1):
            print("*",end=" ")
        print()

    #inverse pyramid
    for i in range(r-1,0,-1):
        for j in range(r-i):
            print(" ",end=" ")
        for k in range(2*i-1):
            print("*",end=" ")
        print()

diamond(5)