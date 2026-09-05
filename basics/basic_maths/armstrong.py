def armstrong(n):
    power = len(str(n))
    sum = 0
    temp = n

    while(temp != 0):
        digit = temp%10
        sum += digit**power
        temp //= 10

    return sum == n

print(armstrong(100))