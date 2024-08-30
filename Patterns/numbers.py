def numbers(n):
    for i in range(0,n):
        for j in range(n-i,0,-1):
            print(" ",end=" ")
        if i == 0:
            for k in range(1,0,-1):
                 print(k,end=" ")
        else:
            for l in range(1,2*i+2):
                 print(l+1,end=" ")
        print()
    
print(numbers(5))

#         1 
#       2 3 4 
#     2 3 4 5 6
#   2 3 4 5 6 7 8
