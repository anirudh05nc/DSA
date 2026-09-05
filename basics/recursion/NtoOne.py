def NtoOne(n):
    if n < 1:
        return

    print(n)
    NtoOne(n-1)

NtoOne(10)