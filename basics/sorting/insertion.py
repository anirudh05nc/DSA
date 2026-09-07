def insertion(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr

arr = [4, 2, 6, 5, 3 ,7, 8, 3, 1, 7, 5, 4]

print(insertion(arr))