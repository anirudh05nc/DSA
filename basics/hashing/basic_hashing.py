arr = [1, 2, 4, 3, 3, 4, 3, 2, 1, 1, 2, 2, 3, 3, 2 ,2, 4]

freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1

print(freq)