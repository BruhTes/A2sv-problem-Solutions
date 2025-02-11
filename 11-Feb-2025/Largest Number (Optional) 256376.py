# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [str(x) for x in nums]
        arr.sort(key=lambda x:x*10, reverse = True)

        if arr[0] == "0":
            return "0"

        res = "".join(arr)
        return res