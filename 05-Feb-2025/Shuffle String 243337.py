# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled : str = [""] * len(s)

        for i, index in enumerate(indices):
            shuffled[index] = s[i]
        
        return "".join(shuffled)
