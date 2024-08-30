def num(n):
    sum = 0
    m = n
    for i in range(1,n+1):
        sum += m
        m = int((i+1)*str(n))
        
    return sum

n = 5
print(num(n))
# n = 4
# lt = []
# s = ""
# for i in range(n):
#     s += str(n)
#     lt.append(s)
# print(lt)
