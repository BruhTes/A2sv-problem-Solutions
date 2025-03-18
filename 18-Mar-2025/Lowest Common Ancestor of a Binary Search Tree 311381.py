# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getpath(self, root, arr, x):
        if not root:
            return False
        
        arr.append(root.val)

        if root.val == x:
            return True
        
        if self.getpath(root.left, arr, x) or self.getpath(root.right, arr, x):
            return True
        
        arr.pop()
        return False


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []

        self.getpath(root, path1, p.val)
        self.getpath(root, path2, q.val)

        i = 0
        while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
            i += 1
        
        return TreeNode(path1[i - 1])