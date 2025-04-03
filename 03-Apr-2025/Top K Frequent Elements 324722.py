# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        # index represents freq
        buckets = [[] for i in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        # return the k most frequent
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                result.extend(buckets[i])
            if len(result) == k:
                return result 
        # return result