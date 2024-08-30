def spiral_traversal(matrix):
    left = 0
    right = len(matrix)-1
    top = 0
    bottom = len(matrix)-1
    lt = []
    while left <=right and top <= bottom:
       
       for i in range(left,right+1):
         lt.append(matrix[top][i])

       top += 1

       for j in range(top,bottom+1):
         lt.append(matrix[j][right])
        
       right -= 1
       if top <= bottom:
        for k in range(right,left-1,-1):
          lt.append(matrix[bottom][k])
        bottom -= 1
    
       if left <= right:
        for l in range(bottom,top-1,-1):
          lt.append(matrix[l][left])

        left += 1


    return ','.join(map(str,lt))

matrix = [
          [1, 2, 3, 4, 5],
          [16,17,18,19,6],
          [15,24,25,20,7],
          [14,23,22,21,8],
          [13,12,11,10,9]
          ]
print(spiral_traversal(matrix))