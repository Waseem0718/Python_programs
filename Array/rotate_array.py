def rotate_array(arr,k):
    n = len(arr)
    k = k % n
    
    temp_array = [0]*n
    
    for i in range(n-k,n):
        temp_array[i- n + k] = arr[i] 
       
    for i in range(0,n-k):
        temp_array[i+k] = arr[i]

    x = ' '.join(map(str,temp_array))
    return x
        
       

arr = [1,2,3,4,5,6,7]    
k = 2
print(rotate_array(arr, k))

# def rotate_array_by_left(arr,k):
#     n = len(arr)
#     k = k % n
    
#     temp_array = [0]*n
    
#     for i in range(k,n):
#         temp_array[i-k] = arr[i] 
       
#     for i in range(0,k):
#         temp_array[n-k + i] = arr[i]
        
       
#     x = ' '.join(map(str,temp_array))
#     return x
# arr = [1,2,3,4,5,6,7]    
# k = 2
# print(rotate_array_by_left(arr, k))
