# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        i = 0
        j = len(piles) - 1
        while j - i + 1 > 3:
            total += piles[j - 1]
            j -= 2
            i += 1
        total += piles[j - 1]
        return total