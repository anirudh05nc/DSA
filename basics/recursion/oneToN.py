def oneToN(i, n):
    if i>n:
        return
    print(i)
    oneToN(i+1, n)

oneToN(1, 10)