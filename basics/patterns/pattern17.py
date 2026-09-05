def pattern17(n):
    for i in range(n):
        for j in range(n-i):
            print(" ",end="")
        for j in range(i):
            print(chr(j+65), end="")
        for j in range(i, -1, -1):
            print(chr(j+65),end="")
        
        print()

pattern17(5)