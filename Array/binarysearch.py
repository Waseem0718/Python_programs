def binarysearch(arr,k,n):
    arr.sort()
    low = 0
    high =n-1
    while low <= high:

        mid = (low+high)//2

        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [1,2,3,4,5,6,7,8,9]
k = 9
n = len(arr)
print("Element found at index",binarysearch(arr,k,n))