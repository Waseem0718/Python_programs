#Count sub array sum equals K
def  subarray(n,arr,k):
    count = 0
    for i in range(n):
         total = 0
         for j in range(i,n):
              total = total + arr[j]
              
              if total == k:
                   count += 1
                    
    return count

arr = [3,1,2,4]
n = len(arr)
k = 6
print(subarray(n,arr,k))


                   


