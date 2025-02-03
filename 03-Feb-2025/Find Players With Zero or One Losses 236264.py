# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loosers = {}
        winners = set()

        for match in matches:
            winner, looser = match
            winners.add(winner)
            loosers[looser] = loosers.get(looser, 0) + 1
    
        no_loss = [player for player in winners if player not in loosers]
        one_loss = [player for player, value in loosers.items() if value == 1]
            
        return [sorted(no_loss), sorted(one_loss)]
