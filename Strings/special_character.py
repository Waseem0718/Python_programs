def sc(s):
    special = "!@#$%^&*()_+<>\"/.,[}{]|"
    for ch in s:
        if ch in special:
            return "string has special character"
    else:
        return "not have a special character"
    
s = "hi how are you"
print(sc(s))
