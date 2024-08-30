#find total sum from the position which is given by the user by doing abs difference
def findtotalsum(n,arr,k):
    total = 0
    for i in range(k,n):
        total += abs(arr[i]-arr[i-1])

    return total

arr = [11,22,12,24,13,26,14]
n = len(arr)
k = 5
print(findtotalsum(n,arr,k))