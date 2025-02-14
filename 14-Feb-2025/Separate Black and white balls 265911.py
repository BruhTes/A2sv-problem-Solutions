# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps = 0
        blackCount = 0

        for char in s:
            if char == "0":
                swaps += blackCount
            else:
                blackCount += 1
        
        return swaps