def remove_outer_paraenthesis(str):
    count = 0
    ans = ""
    for i in str:
        if i =='(':
            if count > 0: # To ignore outermost left parenthesis
                ans += i
            count += 1
        else:
            if i == ")":
                count -= 1 # To ignore outermost right parenthesis
                if count > 0:
                    ans += i

    return ans

str = "((()()))"
print(remove_outer_paraenthesis(str))
                    




