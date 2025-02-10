# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            self.swap(row)
        for row in image:
            self.invert(row)
        return image

    def swap(self, row):
        left = 0
        right = len(row) - 1

        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1

    def invert(self, row):
        for i, num in enumerate(row):
            if num == 0:
                row[i] = 1
            else:
                row[i] = 0