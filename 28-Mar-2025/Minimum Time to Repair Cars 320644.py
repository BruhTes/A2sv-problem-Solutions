# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepair(time):
            count = 0
            for rank in ranks:
                count += int(math.sqrt(time / rank))
            return count >= cars
        
        ranks.sort()
        low, high = 1, ranks[-1] * (cars ** 2)
        ans = -1

        while high >= low:
            mid = low + (high - low) // 2

            if canRepair(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans