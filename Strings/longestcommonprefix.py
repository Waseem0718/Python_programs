def longestcommonprefix(str):
    ans = ""
    str = sorted(str)
    first = str[0]
    last = str[-1]
    for i in range(min(len(first),len(last))):
            if first[i] == last[i]:
                ans += first[i]
            else:
                 break
    return ans


        



str =  input().split()
print(longestcommonprefix(str))