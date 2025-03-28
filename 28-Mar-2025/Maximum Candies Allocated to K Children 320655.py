# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canAllocate(count):
            curr = 0
            for candy in candies:
                curr += (candy) // count
            return curr >= k

        candies.sort()
        low, high = 1, candies[-1]
        ans = 0
        while high >= low:
            mid = low + (high - low) // 2

            if canAllocate(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans