# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixModulo = 0
        seen_modulos = {0 : -1}

        for i, num in enumerate(nums):
            prefixModulo = (prefixModulo + num) % k

            if prefixModulo in seen_modulos:
                if i - seen_modulos[prefixModulo] > 1:
                    return True
            else:
                seen_modulos[prefixModulo] = i
        return False