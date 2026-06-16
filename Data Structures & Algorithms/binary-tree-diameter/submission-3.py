# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def findH(node):
            if not node:
                return 0
            res = max(findH(node.left), findH(node.right))
            return 1 + res

        res = 0
        def dfs(node):
            if not node:
                return
            nonlocal res
            res = max(res, findH(node.left) + findH(node.right))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res