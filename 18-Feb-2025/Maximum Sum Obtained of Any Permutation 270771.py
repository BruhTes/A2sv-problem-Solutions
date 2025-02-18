# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = (10 ** 9) + 7
        indexContribution = [0 for i in range(len(nums))]
        
        for start, end in requests:
            indexContribution[start] += 1
            if end + 1 < len(indexContribution):
                indexContribution[end + 1] -= 1
        
        for i in range(1, len(nums)):
            indexContribution[i] = indexContribution[i - 1] + indexContribution[i]
        
        # sorting both so that we can map the largest contribution to the largest number in nums
        indexContribution.sort(reverse = True)
        nums.sort(reverse = True)        
        
        maxSum = 0
        for i in range(len(indexContribution)):
            maxSum += nums[i] * indexContribution[i]
        
        return (maxSum) % mod