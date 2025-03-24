# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, curr):
            if not root:
                return
            
            curr = (curr * 10) + root.val

            if not root.left and not root.right:
                self.result += curr
                curr -= root.val
                return

            dfs(root.left, curr)
            dfs(root.right, curr)
        
        dfs(root, 0)
        return self.result
