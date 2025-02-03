# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered_nums = 0
        for i in range(left, right + 1):
            for interval in ranges:
                if i >= interval[0] and i <= interval[1]:
                    covered_nums += 1
                    break
        
        return covered_nums == (right - left + 1)