# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        self.depths = []
        if not root:
            return 0
        self.findDepths(root, res)
        return max(self.depths)
    def findDepths(self, root, curDepth):
        if not root:
            self.depths.append(curDepth)
            return
        self.findDepths(root.left, curDepth + 1)
        self.findDepths(root.right, curDepth + 1)
        
        