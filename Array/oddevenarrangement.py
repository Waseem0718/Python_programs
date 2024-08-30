#sort the elements in odd postion in descending order and even position in ascending order
def odd_even_position(arr):
    odd = []
    even = []
    for i in range(len(arr)):
        if i%2==0:
            odd.append(arr[i])
        else:
            even.append(arr[i])

    odd.sort(reverse=True)
    even.sort()

    result = []
    if len(odd) < len(even):
        for i in range(len(odd)):
            arr[2*i] = odd[i]
            arr[2*i+1] = even[i]

        index = 2*len(odd)
        for i in range(len(even)-len(odd)):
            arr[index] = even[len(odd)+i]
            index += 1

    else:
        for i in range(len(even)):
            arr[2*i] = odd[i]
            arr[2*i+1] = even[i]

        index = 2*len(even)
        for i in range(len(odd)-len(even)):
            arr[index] = odd[len(even)+i]
            index += 1

    
    return ','.join(map(str,arr))

arr = [13,2,4,15,12,10,5]
print(odd_even_position(arr))