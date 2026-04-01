# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def findGoodNodes(node, curMax, res):
            if not node:
                return 0
            if node.val >= curMax:
                res = 1
                curMax = node.val
            else:
                res = 0
            return res + findGoodNodes(node.left, curMax, res) + findGoodNodes(node.right, curMax, res)
        
        return findGoodNodes(root, root.val, 0)
        