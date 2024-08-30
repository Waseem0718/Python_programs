def find_min_of_all_greater(arr):
    mini = float("inf")
    for i in range(len(arr)):
        l = 0
        for j in range(l,len(arr)):
            if arr[i] < arr[j]:
                mini = min(mini,arr[j])


        print(arr[i],"->",mini,end=",")
        
        mini = float("inf")

arr = [2,3,7,12,-1,8,5,11,13]
find_min_of_all_greater(arr)