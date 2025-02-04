# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for row in accounts:
            max_wealth = max(max_wealth, sum(row))

        return max_wealth

# Time = O(n)
# Space = O(1)kee