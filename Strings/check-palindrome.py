def check_palindrome(s):
    st = set()
    for ch in s:
        if ch in st:
            st.remove(ch)
        else:
            st.add(ch)

    return len(st) <= 1

s = "carrace"
print(check_palindrome(s))