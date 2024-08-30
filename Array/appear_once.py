def appear_once(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] = freq.get(num,0)+1
        else:
            freq[num] = 1

    for key,value in freq.items():
        if value == 1:
            return key
        
arr = map(int,input().split())
print(appear_once(arr))

# # using XOR
# def appear_once(arr):
#     xor = 0
#     for num in arr:
#         xor ^= num

#     return xor

# arr = map(int,input().split())
# print(appear_once(arr))


