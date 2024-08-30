def hollow_pyramid(n,k):

    for i in range(1,n+1):
        for j in range(1,n*2):
            if  i+j == n+1 or j-i == n-1:
                print("*",end="")
            elif i == n and j != k:
                print("*",end="")
                k += 2
            else:
                print(end=" ")
        print()

n = 5
k = 2

hollow_pyramid(n,k)