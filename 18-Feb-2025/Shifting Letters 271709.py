# Problem: Shifting Letters - https://leetcode.com/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        result = []
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] = shifts[i] + shifts[i + 1]
        
        print(shifts)
        for i, char in enumerate(s):
            new_char = (ord(char) - ord('a') + shifts[i]) % 26
            result.append(chr(new_char + ord('a')))

        return "".join(result)