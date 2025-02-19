# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefixSum = [0] * len(s)
        for row in shifts:
            if row[2] == 0:
                prefixSum[row[0]] -= 1
                if row[1] < len(s) - 1:
                    prefixSum[row[1] + 1] += 1
            else:
                prefixSum[row[0]] += 1
                if row[1] < len(s) - 1:
                    prefixSum[row[1] + 1] -= 1
        
        for i in range(1, len(prefixSum)):
            prefixSum[i] = prefixSum[i - 1] + prefixSum[i]

        result = []
        for i in range(len(s)):
            new_char = chr(((ord(s[i]) - ord('a') + prefixSum[i]) % 26) + ord('a'))
            result.append(new_char)

        return "".join(result)