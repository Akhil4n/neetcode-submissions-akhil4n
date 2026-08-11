# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        vals = []
        def find(node):
            if not node:
                return
            
            find(node.left)
            if len(vals) == k:
                return
            vals.append(node.val)
            find(node.right)
        
        find(root)
        print(vals)
        return vals[k - 1]

            

            





