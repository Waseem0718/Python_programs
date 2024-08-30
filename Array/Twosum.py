#check if pair with a given sum exist in the array
def twosum(arr,n,k):
    total = 0
    for i in range(0,n-1):
        r = i + 1
        while r<n:
            total = arr[i] + arr[r]
            if total == k:
                return arr[i],arr[r]
            r = r + 1
        # for j in range(i+1,n):
        #     total = arr[i] + arr[j]
        #     if total == k:
        #         return arr[i],arr[j]
        
arr = [2,1,1,17,18,3]
n = len(arr)
k = 21
print(twosum(arr,n,k))