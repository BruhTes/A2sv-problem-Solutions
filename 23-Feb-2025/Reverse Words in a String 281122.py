# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        ans = s.split()
        left = 0
        right = len(ans) - 1
        while left < right:
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1
        ans = " ".join(ans)
        return ans