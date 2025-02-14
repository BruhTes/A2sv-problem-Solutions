# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        i = 0
        while i < len(costs) and coins >= 0:
            coins -= costs[i]
            i += 1
        
        return i - 1 if coins < 0 else i
                