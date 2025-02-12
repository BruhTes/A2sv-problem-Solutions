# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        goal = skill[0] + skill[-1]

        left = 0
        right = len(skill) - 1
        chemistry = 0
    
        while left < right:
            if skill[left] + skill[right] != goal:
                return -1
            else:
                chemistry += (skill[left] * skill[right])

            left += 1
            right -= 1
        
        return chemistry