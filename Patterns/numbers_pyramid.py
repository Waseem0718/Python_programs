# def pattern(n):
#     for i in range(n,0,-1):
#         for j in range(i,0,-1):
#             print(n,end="")
#         n -= 1
#         print()
    
# pattern(4)

# 4444
# 333
# 22
# 1

def num_in_pyramid(n):
   for i in range(1,n+1):
        for j in range(n-i+1):
            print(" ",end=" ")
    

        for k in range(i,0,-1):
            print(k,end=" ")

        for k in range(2,i+1):
            print(k,end=" ")
        print()
num_in_pyramid(4)     

#         1 
#       2 1 2 
#     3 2 1 2 3
#   4 3 2 1 2 3 4