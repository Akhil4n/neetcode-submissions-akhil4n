# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        max_val = max(p.val, q.val)
        min_val = min(p.val, q.val)
        while curr:
            if curr.val > max_val:
                curr = curr.left
            elif curr.val < min_val:
                curr = curr.right
            else:
                return curr
        
