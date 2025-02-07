# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = (left + right) // 2

            if letters[mid] == target:
                if mid == len(letters) - 1:
                    break
                elif letters[mid + 1] > target:
                    return letters[mid + 1]
                else:
                    left = mid + 1

            elif letters[mid] > target:
                if letters[mid - 1] < target:
                    return letters[mid]
                else:
                    right = mid - 1

            else:
                left = mid + 1
                
        return letters[0]  