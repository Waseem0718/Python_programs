def stock(arr,n):
    maxi = float("-inf")
    profit = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] > arr[i]:
                profit = arr[j] - arr[i]
                maxi = max(maxi,profit)

            # elif arr[j] < arr[i]:
            #     i += 1
            #     j +=1

    return maxi

arr = [7,1,5,4,8,2]
n = len(arr)
print(stock(arr,n))


#using one loop
def stock(arr,n):
    mini = float("inf")
    maxi = 0
    for i in range(n):
        mini = min(mini,arr[i])
        maxi = max(maxi,arr[i]-mini)

    return maxi

arr = [7,1,5,4,8,2]
n = len(arr)
print(stock(arr,n))