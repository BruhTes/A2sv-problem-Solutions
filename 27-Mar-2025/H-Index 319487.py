# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        left, right = 0, len(citations) - 1
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            
            if citations[mid] >= len(citations) - mid:
                ans = len(citations) - mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
