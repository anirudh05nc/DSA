def missingNum(self, arr):
        # code here
        length = len(arr)
        sum1 = sum(arr)
        
        n = length + 1
        total_sum = (n * (n+1))//2
        
        return total_sum-sum1