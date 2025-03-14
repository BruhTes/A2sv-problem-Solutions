# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if not root:
            return result
        
        curr = [root]

        while curr:
            node = curr.pop()
            result.append(node.val)

            if node.right:
                curr.append(node.right)
            if node.left:
                curr.append(node.left)
        
        return result
            

