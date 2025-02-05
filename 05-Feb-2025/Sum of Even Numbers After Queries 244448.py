# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evens = []
        Sum = sum(x for x in nums if x % 2 == 0)
        
        for val, index in queries:
            if nums[index] % 2 == 0:
                Sum -= nums[index]
            nums[index] += val

            if nums[index] % 2 == 0:
                Sum += nums[index]
            
            evens.append(Sum)

        return evens