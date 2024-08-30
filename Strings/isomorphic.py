def isomorphic(s,t):
    s_t = {} 
    t_s = {}
    if len(s)!=len(t):
        return False
    for ch_s,ch_t in zip(s,t):
        if ch_s in s_t and s_t[ch_s] != ch_t:
            return False
        else:
            s_t[ch_s] = ch_t
        
        if ch_t in t_s and t_s[ch_t] != ch_s:
            return False
        else:
            t_s[ch_t] = ch_s
    
    return True
        
s = "add"
t = "see"
print(isomorphic(s,t))