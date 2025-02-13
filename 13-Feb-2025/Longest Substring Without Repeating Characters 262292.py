# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = {}
        max_len = 0

        left = 0
        for right in range(len(s)):
            if s[right] in counter:
                left = max(left, counter[s[right]] + 1)

            counter[s[right]] = right
            max_len = max(max_len, right - left + 1)
        
        print(counter)
        return max_len
