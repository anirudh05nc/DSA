def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        curr_len = 0

        for i in nums:
            if i == 1:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 0
        
        return max(max_len, curr_len)