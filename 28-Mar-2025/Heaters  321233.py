# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        def canWarn(radius):
            heater_index = 0
            for house in houses:
                while (heater_index < len(heaters) - 1 and 
                    abs(heaters[heater_index] - house) >= 
                    abs(heaters[heater_index + 1] - house)):
                    heater_index += 1
                
                # Check if the closest heater can heat the house within the given radius
                if abs(heaters[heater_index] - house) > radius:
                    return False
            
            return True
        
        # Binary search for minimum radius
        low, high = 0, max(heaters[-1] - houses[0], houses[-1] - houses[0])
        
        while low <= high:
            mid = low + (high - low) // 2
            if canWarn(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low