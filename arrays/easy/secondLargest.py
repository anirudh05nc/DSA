def getSecondLargest(self, arr):
    
    if len(arr) == 1:
        return -1
    
    lar = float('-inf')
    sec_lar = float('-inf')
    
    for num in arr:
        if num > lar:
            sec_lar = lar
            lar = num
        elif num > sec_lar and num != lar:
            sec_lar = num
            
    if lar == float('-inf') or sec_lar == float('-inf'):
        return -1
    else:
        return sec_lar