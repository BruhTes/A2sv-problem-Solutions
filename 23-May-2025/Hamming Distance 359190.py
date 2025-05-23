# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        m = 1
        count = 0
        while num >= m:
            if m & num == m:
                count += 1
            m *= 2
        return count

        