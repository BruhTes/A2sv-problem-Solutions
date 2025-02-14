# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        count = [0] * (max_cost + 1)
        for cost in costs:
            count[cost] += 1
        
        barsCount = 0
        for cost, freq in enumerate(count):
            while freq > 0 and coins >= 0:
                coins -= cost
                freq -= 1
                barsCount += 1
        
        return barsCount - 1 if coins < 0 else barsCount            