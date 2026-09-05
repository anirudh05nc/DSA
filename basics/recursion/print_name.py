def print_name(name, curr, n):
    if curr > n:
        return
    print(name)
    print_name(name, curr+1, n)

print(print_name("Anirudh", 1, 10))
