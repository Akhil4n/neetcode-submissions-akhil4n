# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:


        def add(curr):
            if not curr:
                return TreeNode(val)

            if curr.val > val:
                curr.left = add(curr.left)
            else:
                curr.right = add(curr.right)
            return curr
        
        return add(root)
        