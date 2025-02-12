# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1
        count = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
                left += 1
            else:
                right -= 1
            count += 1
        return count
            