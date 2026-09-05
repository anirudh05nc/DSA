class Solution:
    def reverseString(self, left, right, string):
        if left > right:
            return string

        temp = string[left]
        string[left] = string[right]
        string[right] = temp

        return self.reverseString(left+1, right-1, string)

    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for ch in s:
            if ch.isalnum():
                new_s.append(ch.lower())
        
        original = new_s.copy()

        ans = self.reverseString(0, len(new_s)-1, new_s)

        return ans == original


        