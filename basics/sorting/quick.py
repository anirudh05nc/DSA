def quick(arr, low, high):
    if low >= high:
        return
    
    pivot = arr[high]
    left = low-1
    for i in range(low, high):
        if arr[i] < pivot:
            left += 1
            arr[left], arr[i] = arr[i], arr[left]

    left += 1
    arr[left], arr[high] = arr[high], arr[left]

    quick(arr, low, left-1)
    quick(arr, left+1, high)
    

arr = [4, 2, 6, 5, 3 ,7, 8, 1]

print(quick(arr, 0, len(arr)-1))

print(arr)