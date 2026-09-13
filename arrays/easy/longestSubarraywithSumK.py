def longestSubarray(self, nums, k):
        n = len(nums)
        
        maxLen = 0
        
        left = 0
        right = 0
        
        sum = nums[0]
        
        while right < n:
            
            while left <= right and sum > k:
                sum -= nums[left]
                left += 1
            
            if sum == k:
                maxLen = max(maxLen, right - left + 1)
            
            right += 1
            if right < n:
                sum += nums[right]
        
        return maxLen


class SubarraySolver:
    def get_longest_subarray(self, a, k):
        n = len(a)
        pre_sum_map = {}  # Dictionary to store prefix_sum -> first index
        sum_so_far = 0    # Running sum
        max_len = 0       # Max length of subarray with sum = k

        for i in range(n):
            sum_so_far += a[i]  # Update running sum

            # Case 1: Entire subarray from index 0 to i has sum = k
            if sum_so_far == k:
                max_len = i + 1

            # Case 2: If (sum_so_far - k) exists in map, we found a valid subarray
            rem = sum_so_far - k
            if rem in pre_sum_map:
                length = i - pre_sum_map[rem]
                max_len = max(max_len, length)

            # Store the first occurrence of the current prefix sum
            if sum_so_far not in pre_sum_map:
                pre_sum_map[sum_so_far] = i

        return max_len

# Example usage
a = [2, 3, 1, 2, -1]
k = 3
solver = SubarraySolver()
length = solver.get_longest_subarray(a, k)
print("The length of the longest subarray is:", length)
