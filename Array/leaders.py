def leader(arr):
    temp= []
    n =  len(arr)
    maxi = arr[n-1]
    temp.append(arr[n-1])
    for i in range(n-2,-1,-1):
        if arr[i] > maxi:
            temp.append(arr[i])
            maxi = arr[i]

    temp.sort(reverse=True)
    return temp


arr = [30,10,22,12,3,0,6]
print(leader(arr))


         