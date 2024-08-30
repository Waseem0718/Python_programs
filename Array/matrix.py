# def matrix(arr):



row = 3
col = 3
matrix = []
for i in range(row):
    row = list(map(int,input().split()))
    matrix.append(row)
n = len(matrix)
total = 0
for r in matrix:
    total += sum(r)

diagonal1,diagonal2 = 0,0

for i in range(n):
    diagonal1 += matrix[i][i]
    diagonal2 += matrix[i][n-i-1]

total_diagonal = diagonal1 + diagonal2




print(total)
print(total_diagonal)