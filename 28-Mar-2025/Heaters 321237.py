# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        if not heaters or not houses:
            return 0
        
        if len(heaters) == 1:
            return max(heaters[-1] - houses[0], houses[-1] - houses[0])

        # find the maximum of the minimum distance needed for each houses
        result = 0
        heater_pos = 0
        for house in houses:
            # find its next heater
            while heater_pos < len(heaters) - 1 and house > heaters[heater_pos]:
                heater_pos += 1

            # Check distance to current and previous heater
            if heater_pos == 0:
                r = heaters[heater_pos] - house
            elif heater_pos == len(heaters):
                r = house - heaters[-1]
            else:
                r = min(abs(house - heaters[heater_pos-1]), abs(heaters[heater_pos] - house))
            result = max(result, r)
        
        return result