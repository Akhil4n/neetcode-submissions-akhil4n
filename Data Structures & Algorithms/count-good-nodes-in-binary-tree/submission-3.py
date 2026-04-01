# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curMax = float('-inf')
        def dfs(node, curMax):
            if not node:
                return 0
            if node.val >= curMax:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            else:
                return 0 + dfs(node.left, curMax) + dfs(node.right, curMax)
        return dfs(root, curMax)