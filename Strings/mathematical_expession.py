def mathematicalexpression(s):
    stack = []
    operators = {"+-/*"}
    previous_char = ""
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1]!='(':
                return "Invalid"
            stack.pop()
            
        elif ch.isalnum():
            previous_char = ch
        elif ch in operators:
            if previous_char is None or previous_char in operators or previous_char=='(':
                return "Invalid"
            previous_char = ch
        else:
            return "Invalid"
        
    if stack:
        return "Invalid"
    
    if previous_char in operators:
        return "Invalid"
    
    return "Valid"


s = "a+b"
print(mathematicalexpression(s))
        
