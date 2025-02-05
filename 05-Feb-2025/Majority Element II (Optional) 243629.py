# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elements = []
        n = len(nums)
        nums = Counter(nums)
        
        for key in nums:
            if nums[key] > (n // 3):
                elements.append(key)
        return elements