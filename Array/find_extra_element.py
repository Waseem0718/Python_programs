def find_extra_elt(arr1,arr2):
    if len(arr1) > len(arr2):
        for ch in arr1:
            if ch not in arr2:
                return ch, arr1.index(ch)
    
    else:
        for ch in arr2:
            if ch not in arr1:
                return ch, arr2.index(ch)

        
    

arr1 = [10,20,30,5]
arr2 = [10,5,30,20,12]
print(find_extra_elt(arr1,arr2))
