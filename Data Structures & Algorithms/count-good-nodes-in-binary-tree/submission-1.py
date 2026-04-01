# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        curMax = float("-inf")
        self.dfs(root, curMax)
        return self.res
    def dfs(self, node, curMax):
            if not node:
                return
            if node.val >= curMax:
                self.res += 1
                curMax = node.val
            self.dfs(node.left, curMax)
            self.dfs(node.right, curMax)
        