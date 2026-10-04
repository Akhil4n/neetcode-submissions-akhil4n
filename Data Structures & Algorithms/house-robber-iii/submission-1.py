# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node):
            if not node:
                return (0, 0)

            left = traverse(node.left)
            right = traverse(node.right)
            curr = node.val

            return (curr + left[1] + right[1], max(left[0] + right[0], left[0] + right[1], left[1] + right[0], left[1] + right[1]))

        res = traverse(root)
        return max(res)
            