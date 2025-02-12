# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        total = sum(skill)

        if total % (n // 2) != 0:
            return -1
        
        target = total // (n // 2)
        counter = Counter(skill)
        chemistry = 0

        for key, val in counter.items():
            partner = target - key

            if partner not in counter or counter[partner] != val:
                return -1
            
            chemistry += (partner * key) * val
        
        return chemistry // 2