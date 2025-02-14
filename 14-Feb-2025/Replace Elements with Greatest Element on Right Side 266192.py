# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = arr[-1]
        arr[-1] = -1
        N = len(arr)

        for i in range(N - 2, -1, -1):
            current = arr[i]
            arr[i] = max_num
            max_num = max(max_num, current)
        
        return arr