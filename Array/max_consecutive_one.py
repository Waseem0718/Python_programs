def max_one(arr):
    count = 0
    maxi = 0
    start = 0
    begin,end = 0, 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
            if count == 1:
                start = i
            if count > maxi:
                maxi = count
                begin = start
                end = i
        else:
            count = 0
        

    return arr[begin:end+1],maxi

arr = [1,1,2,1,1,0,1,1,1,1,1,1]
print(max_one(arr))