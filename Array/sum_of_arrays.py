def sum_of_array(arrays):
    sum = 0
    for array in arrays:
       digits = ''.join(map(str,array))
       sum += int(digits)

    return sum

n =int(input())
arrays = []
for i in range(n):
    array = input(f"Enter elements of array {i+1} separated by space: ").split()
  
    array = [int(x) for x in array]
 
    arrays.append(array)
print(sum_of_array(arrays))