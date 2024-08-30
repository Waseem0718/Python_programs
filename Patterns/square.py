def square(n):
    num = 1
    for i in range(1):
        for j in range(1,n+1):
            print(num,end=" ")
            num += 1
        print()
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i+j == n+i:
                print(num,end=" ")
                num += 1
            else:
                print( end=" ")
                
        print()
    
square(5)