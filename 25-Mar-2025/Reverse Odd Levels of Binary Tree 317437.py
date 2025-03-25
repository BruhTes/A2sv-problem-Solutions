# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # use dictionary to store list of nodes at each level while doing dfs
        def dfs(root, level, nodes_at_levels):
            if not root:
                return
            
            if level % 2 == 1:
                if level not in nodes_at_levels:
                    nodes_at_levels[level] = []
                nodes_at_levels[level].append(root)
            
            dfs(root.left, level + 1, nodes_at_levels)
            dfs(root.right, level + 1, nodes_at_levels)
        
        # reverse the levels stored in the dictionary
        def reverseLevels(nodes_at_levels):
            for level in nodes_at_levels:
                levelNodes = nodes_at_levels[level]

                left, right = 0, len(levelNodes) - 1

                while left < right:
                    levelNodes[left].val, levelNodes[right].val = levelNodes[right].val, levelNodes[left].val
                    left += 1
                    right -= 1
        
        nodes_at_levels = {}
        dfs(root, 0, nodes_at_levels)
        reverseLevels(nodes_at_levels)
        return root