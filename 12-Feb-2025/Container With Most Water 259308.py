# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0

        left = 0
        right = len(height) - 1

        while left <= right:
            if height[left] > height[right]:
                area = max(area, (right - left) * height[right])
                right -= 1
            else:
                area = max(area, (right - left) * height[left])
                left += 1
        return area
        