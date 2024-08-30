def unbalanced_parenthesis(string):
    stack = []
    for ch in string:
        if ch == "(":
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                return "Unbalanced parenthesis"

    if not stack: 
        return "Balanced Parenthesis"
    else:
        return "unbalanced parenthesis"
    
string = "((((())))"
    
print(unbalanced_parenthesis(string))

