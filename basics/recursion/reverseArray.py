def reverseArray(left, right, arr):
    if (left > right):
        return

    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    reverseArray(left+1, right-1, arr)


arr = [1, 2, 3, 4, 5]
print(arr)
reverseArray(0, len(arr)-1, arr)

print(arr)