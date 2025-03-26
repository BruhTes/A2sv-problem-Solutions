# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def good(index):
            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i] / index)
            return h >= time
        
        left, right = 1, max(piles)
        idx = 1
        while left <= right:
            mid = left + (right - left) // 2

            if good(mid):
                idx = mid
                right = mid - 1
            else:
                left = mid + 1
        return idx