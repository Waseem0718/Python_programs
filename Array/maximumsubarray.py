# def maximum_subarray(arr): #Kadane's Algorithm
#     maxi = float("-inf")
#     sum = 0
#     for i in range(0,len(arr)):
         
        
         
#          sum += arr[i]

#          if sum > maxi:
#               maxi = sum

#          if sum < 0:
#               sum = 0

#     return maxi

# if __name__ == "__main__":
#      arr = [-2,-3,1,3,-1,5,-4,4,1]
#      print(maximum_subarray(arr))


def maximum_subarray(arr): #Kadane's Algorithm to print subarray of maximum sm
    maxi = float("-inf")
    sum = 0
    start = 0
    begin , end = -1, -1
    for i in range(0,len(arr)):
         
         if sum == 0:
              start = i
         
         sum += arr[i]

         if sum > maxi:
              maxi = sum
              begin = start
              end = i

         if sum < 0:
              sum = 0

    return arr[begin:end+1],maxi

if __name__ == "__main__":
     arr = [-2,-3,1,3,-1,5,-4,4,1]
     print(maximum_subarray(arr))

