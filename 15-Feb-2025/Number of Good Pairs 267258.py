# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_nums = defaultdict(int)
        count = 0

        for num in nums:
            count += hash_nums[num]
            hash_nums[num] += 1

        return count