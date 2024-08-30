def inverted_hollow_py(n):
  
    for i in range(0,n):
        for j in range(0,n):
            if i == 0 or j == n-1 or j == i:
                print("* ",end="")
            else:
                print(end="  ")
        print()

inverted_hollow_py(5)