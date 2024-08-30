def pattern(str):
    for i in range(0,len(str)):
        ind = 0
        print(str[ind:i+1],end="")
        print()
str = "python"
pattern(str)