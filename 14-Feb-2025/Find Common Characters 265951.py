# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        commons = Counter(words[0])

        for i in range(1, len(words)):
            current = Counter(words[i])

            for key in list(commons.keys()):
                if key not in current:
                    del commons[key]
                else:
                    commons[key] = min(commons[key], current[key])

        for key, count in commons.items():
            result.extend([key] * count)

        return result