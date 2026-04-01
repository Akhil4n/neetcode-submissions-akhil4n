# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        iterations = 0
        res = None
        def inorder(node):
            nonlocal iterations, res
            if not node or res is not None:
                return
            inorder(node.left)
            iterations += 1
            if iterations == k:
                res = node.val
                return
            inorder(node.right)
        inorder(root)
        return res
            
            