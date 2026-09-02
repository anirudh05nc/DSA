def pattern14(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j), end='')
        print()
    

pattern14(7)