def sortarray(arr):
    n = len(arr)
    mid,low = 0,0
    high = n-1
    while mid < high:
        if arr[mid] == 0:
            arr[mid],arr[low] =arr[low], arr[mid]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            arr[mid],arr[high] =arr[high], arr[mid]
            high -= 1
        else:
            mid += 1

    return arr

arr = [2,0,1,0,2,1]
print(sortarray(arr))