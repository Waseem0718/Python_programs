def maxmin(arr):
    length = len(arr)
    mid = length//2

    mini = []
    maxi = []
    for num in arr:
        if num >= arr[mid]:
            maxi.append(num)
        else:
            mini.append(num)

    maxi.sort(reverse=True)
    
    for i in range(len(maxi)):
        arr[2*i] = maxi[i]
    for i in range(len(mini)):
        arr[2*i+1] = mini[i]

    return arr

arr = [1,2,3,4,5,6,7]
print(maxmin(arr))