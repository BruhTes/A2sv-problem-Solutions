# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        Sum = 0
        
        for word in words:
            count = Counter(word)

            for key in count:
                possible = True
                if count[key] > chars.get(key, 0):
                    possible = False
                    break
                
            if possible:
                Sum += len(word)
                
        return Sum