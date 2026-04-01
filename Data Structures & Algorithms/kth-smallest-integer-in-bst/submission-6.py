# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.res = None
        self.inorderTraversal(root)
        return self.res
    def inorderTraversal(self, node):
            if not node:
                return
            self.inorderTraversal(node.left)
            self.count -= 1
            if self.count == 0:
                self.res = node.val
                return
            self.inorderTraversal(node.right)
