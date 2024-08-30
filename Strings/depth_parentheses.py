def depth_parentheses(str):
    ans = 0
    stack = []
    for ch in str:
        if ch=="(":
            stack.append(ch)
        elif ch==")":
            stack.pop()
        ans = max(ans,len(stack))

    return ans

str = "((1+(2+3)+((8)/4))+1)"
print(depth_parentheses(str))
