# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        mVal = float('-inf')
        if not root:
            return 0
        self.findGoods(root, mVal)
        return self.res
    def findGoods(self, node, mVal):
            if not node:
                return
            if node.val >= mVal:
                self.res += 1
                mVal = node.val
            self.findGoods(node.left, mVal)
            self.findGoods(node.right, mVal)
        