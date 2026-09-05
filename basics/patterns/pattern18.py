def pattern18(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(chr(64+n-i+j),end="")
        
        print()

pattern18(5)