# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(nums):
            for i, n in enumerate(nums):
                if n == 0:
                    nums[i] = 1
                else:
                    nums[i] = 0
            return nums
        
        def reverse(string, l, r):
            while l < r:
                string[r], string[l] = string[l], string[r]
                r -= 1
                l += 1
            return string
        
        def buildString(n):
            if n == 1:
                return [0]

            current = buildString(n - 1)
            current = current + [1] + reverse(invert(current), 0, len(current) - 1)
            
            return current
    
        current = buildString(n)

        return str(current[k - 1])