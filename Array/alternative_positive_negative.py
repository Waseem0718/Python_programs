def atlernative(arr):
    pos = []
    neg = []
    for num in arr:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)

    if len(pos) < len(neg):
        for i in range(len(pos)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]

        index = 2*len(pos)
        for i in range(len(neg)-len(pos)):
            arr[index] = neg[len(pos)+i]
            index += 1

    else:
        for i in range(len(neg)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]

        index = 2*len(neg)
        for i in range(len(pos)-len(neg)):
            arr[index] = pos[len(neg)+i]
            index += 1

    
    return arr

arr = [1,2,-3,-1,-2,3]
print(atlernative(arr))