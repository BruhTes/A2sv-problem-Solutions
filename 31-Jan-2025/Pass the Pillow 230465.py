# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        complete_rounds = time // (n - 1)

        remaining_moves = time % (n - 1)

        if complete_rounds % 2 == 0:
            return remaining_moves + 1
        else:
            return n - remaining_moves
