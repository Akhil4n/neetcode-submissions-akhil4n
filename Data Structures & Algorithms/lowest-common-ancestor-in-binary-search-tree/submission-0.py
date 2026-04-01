# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            v = curr.val
            if v >= min(p.val, q.val) and v <= max(p.val, q.val):
                return curr
            elif v > p.val and v > q.val:
                curr = curr.left
            elif v < p.val and v < q.val:
                curr = curr.right
            
