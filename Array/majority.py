def majority(arr,n):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] = freq.get(i,0)+1
        else:
            freq[i] = 1
    
    for key,value in freq.items():
        if value >= (n//2):
            return key
        
arr = [1,1,1,1,2,2,2,0]
n = len(arr)
print(majority(arr,n))