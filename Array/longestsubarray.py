def longest_subarray_sum(arr,k,n):
     maxi = 0
     for i in range(n):
          sum = 0
          for j in range(i,n):
               sum += arr[j]

               if sum == k:
                 maxi = max(maxi, j - i + 1)

     return maxi



arr = [1,2,1,2,1,1,1,1]
n = len(arr)
k = 4
print(longest_subarray_sum(arr,k,n))
        
