def maxwindow(s,t):
    mini = float("inf")
    maxi = float("-inf")

    for char in t:
        index = s.find(char)
        if index != -1:
            mini = min(mini,index)
            maxi = max(maxi,index)

    return s[mini:maxi+1]
            
                       


s = "AFBHGCGIUBVCN"
t = "ABC"
print(maxwindow(s,t))