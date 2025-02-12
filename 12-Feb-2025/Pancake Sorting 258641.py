# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start = 0
            while start <= end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        # pancake sort
        indices = []
        for k in range(len(arr) - 1, 1, -1):
            max_idx = arr.index(max(arr[:k+1]))

            if max_idx == k:
                continue
            if max_idx != 0:
                flip(max_idx)
                indices.append(max_idx)

            flip(k)
            indices.append(k)            

        return indices