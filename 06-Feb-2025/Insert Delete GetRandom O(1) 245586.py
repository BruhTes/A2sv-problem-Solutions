# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random

class RandomizedSet:

    def __init__(self):
        self.index_map = {}
        self.list_elemts = []

    def insert(self, val: int) -> bool:
        if val not in self.index_map:
            self.index_map[val] = len(self.list_elemts)
            self.list_elemts.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.index_map:
            index_to_remove = self.index_map[val]

            last_element = self.list_elemts[-1]
            self.list_elemts[index_to_remove] = last_element
            self.index_map[last_element] = index_to_remove

            self.list_elemts.pop()
            del self.index_map[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list_elemts)
