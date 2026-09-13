def largest(self, arr):
    if len(arr) == 1:
        return arr[0]
        
    lar = float('-inf')
    
    for num in arr:
        if num > lar:
            lar = num
    
    if lar == float('-inf'):
        return
    else:
        return lar