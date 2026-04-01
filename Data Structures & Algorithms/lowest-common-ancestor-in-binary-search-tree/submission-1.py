# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findLCA(node):
            bottom, top = min(p.val, q.val), max(p.val, q.val)
            if node.val >= bottom and node.val <= top:
                return node
            if node.val < bottom:
                return findLCA(node.right)
            elif node.val > top:
                return findLCA(node.left)
        return findLCA(root)