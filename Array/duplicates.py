def remove_duplicates(arr):
    n = len(arr)
    temp = []
    for i in arr:
        if i not in temp:
            temp.append(i)

    # temp.sort()
    x = ' '.join(map(str, temp))
    return x

arr = list(map(int,input().split()))
print(remove_duplicates(arr))

