# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(ship_weight):
            days_to_ship = 1
            curr_weight = 0

            for weight in weights:
                curr_weight += weight
                if curr_weight > ship_weight:
                    days_to_ship += 1
                    curr_weight = weight

            return days_to_ship <= days
            
        
        low, high = max(weights), sum(weights)
        ans = -1
        while high >= low:
            mid = low + (high - low) // 2

            if canShip(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans