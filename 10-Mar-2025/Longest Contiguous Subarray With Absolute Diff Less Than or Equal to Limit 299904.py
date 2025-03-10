# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing_queue = deque()
        decreasing_queue = deque()

        length = 0
        left = 0
        for right in range(len(nums)):
            while decreasing_queue and decreasing_queue[-1] < nums[right]:
                decreasing_queue.pop()
            decreasing_queue.append(nums[right])

            while increasing_queue and increasing_queue[-1] > nums[right]:
                increasing_queue.pop()
            increasing_queue.append(nums[right])

            # check limit
            if decreasing_queue[0] - increasing_queue[0] > limit:
                if nums[left] == decreasing_queue[0]:
                    decreasing_queue.popleft()
                if nums[left] == increasing_queue[0]:
                    increasing_queue.popleft()
                left += 1
            
            length = max(length, right - left + 1)
        return length