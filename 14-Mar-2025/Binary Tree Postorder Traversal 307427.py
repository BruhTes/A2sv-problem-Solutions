# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
result = []

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postOrder(root):
            global result

            if not root:
                return
            
            postOrder(root.left)
            postOrder(root.right)
            result.append(root.val)
        
        if result:
            result.clear()
            
        postOrder(root)
        return result