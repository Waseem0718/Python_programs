def longest_cons_seq(arr):
    n = len(arr)
    arr.sort()
    maxi = 0
    count = 1
    for i in range(1,n):
        if (arr[i]-1) == arr[i-1]:
            count += 1
            maxi = max(maxi,count)
        else:
            count = 1
        
    return maxi

arr = [3,5,8,7,6]
print(longest_cons_seq(arr))