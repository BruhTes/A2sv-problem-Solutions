# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, depth):
            if not root:
                return
            
            # if the is not visited yet
            if len(self.result) < depth:
                self.result.append(root.val)
            else:
                self.result[depth - 1] = max(self.result[depth - 1], root.val)
            
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
            

        dfs(root, 1)
        return self.result

