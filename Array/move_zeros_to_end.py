def move_zeros_to_end(arr,k): 
     
#      temp = []
#      for i in range(0,n):
#         if arr[i] != 0:
#             temp.append(arr[i])

#      m = len(temp)
#      for i in range(m,n):
#         temp.append(0)

#      b = map(str,temp)
    
#      a = " ".join(b)
#      return a
    r, l = 0, 0
    while r<len(arr):
        if arr[r] != 0:
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
            l += 1
        r += 1

    return arr            

   

arr = [1,0,2,0,3,4,0,5,6]    
n = len(arr)
print(move_zeros_to_end(arr, n))