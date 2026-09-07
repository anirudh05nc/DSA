
def selection_sort(arr):
    for i in range(len(arr)-1):
        mini = i
        for j in range(i+1, len(arr)):
            mini = j if arr[j] < arr[mini] else mini

        arr[i], arr[mini] = arr[mini], arr[i]
    return arr

arr = [4, 2, 6, 5, 3 ,7, 8, 3, 1, 7, 5, 4]

print(selection_sort(arr))
