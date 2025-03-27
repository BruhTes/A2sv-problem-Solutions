# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def canDistribute(x):
            prev = position[0]
            balls_placed = 1
            
            for i in range(len(position)):
                if position[i] - prev >= x:
                    prev = position[i]
                    balls_placed += 1
                
                if balls_placed == m:
                    return True
            
            return False        
        
        position.sort()
        left, right = 1, math.ceil(position[-1] / (m - 1))
        ans = -1

        while right >= left:
            mid = left + (right - left) // 2

            if canDistribute(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans