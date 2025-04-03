# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.count = 0
        self.dfs(root)
        
        return self.count

    def dfs(self, node):
        if not node:
            return (0, 0)
        
        if not node.left and not node.right:
            self.count += 1
            return (node.val, 1)
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        average = (left[0] + right[0] + node.val) // (left[1] + right[1] + 1)

        if average == node.val:
            self.count += 1
        
        return (
            left[0] + right[0] + node.val, 
            left[1] + right[1] + 1
        )