def union(arr1,arr2):
    temp = []
    for num in arr1:
        temp.append(num)

    for num in arr2:
        if num not in temp:
            temp.append(num)
        
    st = ','.join(map(str,sorted(temp)))
    return st

arr1 = [2,4,5,6,7,9,10,13]
arr2 = [2,3,4,5,6,7,8,9,11,15]
print(union(arr1,arr2))

