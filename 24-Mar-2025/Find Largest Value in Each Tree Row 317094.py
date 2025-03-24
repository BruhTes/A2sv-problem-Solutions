# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = {}

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, depth):
            if not root:
                return
            
            # if the is not visited yet
            if depth in self.result:
                self.result[depth] = max(self.result[depth], root.val)
            else:
                self.result[depth] = self.result.get(depth, 0) + root.val
            
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)


        dfs(root, 0)
        final = []

        for key in self.result:
            final.append(self.result[key])

        return final

