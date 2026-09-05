def sumOfN(i, n):
    if n == 0:
        return i 
    return sumOfN(i+n, n-1)

print(sumOfN(0, 10))