# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, minVal, maxVal):
            if not root:
                return maxVal - minVal
            
            minVal = min(minVal, root.val)
            maxVal = max(maxVal, root.val)

            left_diff = dfs(root.left, minVal, maxVal)
            right_diff = dfs(root.right, minVal, maxVal)

            return max(left_diff, right_diff)
        
        return dfs(root, root.val, root.val)