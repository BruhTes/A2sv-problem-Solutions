# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        changed.sort()
        counter = Counter(changed)
        original = []

        for num in changed:
            if counter[num] > 0:
                if counter[num * 2] > 0:
                    counter[num] -= 1
                    counter[num * 2] -= 1
                    original.append(num)  
                else:
                    return []

        return original
