def productarray(arr,n):
    
    maxi = float('-inf')
    for i in range(0,n):
        product = 1
        for j in range(i,n):
            product = product * arr[j]
            maxi = max(maxi,product)

    return maxi

arr = [1,2,-3,0,-4,-5]
n = len(arr)
print(productarray(arr,n))