def isPalindrome(self, x: int) -> bool:
    if x<0:
        return False

    res = 0
    temp = x

    while temp != 0:
        digit = temp%10
        res = res*10 + digit
        temp = temp//10

    if res == x:
        return True
    
    return False
    