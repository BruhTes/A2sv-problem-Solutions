# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        # pancake sort
        indices = []
        for k in range(len(arr) - 1, 0, -1):
            max_idx = arr.index(max(arr[:k+1]))

            # if the max num is already sorted
            if max_idx == k:
                continue
            # if the max num is not at index 0
            if max_idx != 0:
                flip(max_idx)
                indices.append(max_idx + 1)
            # move the max num to the end of the sub-unsorted-list
            flip(k)
            indices.append(k + 1)            

        return indices