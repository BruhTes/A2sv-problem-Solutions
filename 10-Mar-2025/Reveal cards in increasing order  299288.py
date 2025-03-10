# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = [0] * len(deck)
        queue = deque(range(len(deck)))

        for card in deck:
            i = queue.popleft()
            result[i] = card
            if queue:
                queue.append(queue.popleft())
        return result