'''
input : 1 2 3 4 5
output 
1 5
2 4
3
2 4
1 5
'''

def string(s):
    length = len(s)
    mid = length//2
    upper_part = [f'{s[i]} {s[length-i-1]}' for i in range(mid)]
    lower_part = upper_part[::-1]

    for line in upper_part:
        print(line)

    print(s[mid])

    for line in lower_part:
        print(line)

s ="PROGRAM"
string(s)

    
