# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def find_successor(node):
            while node.left.left:
                node = node.left
            res = node.left
            node.left = res.right
            return res

        def delete(node):
            if not node.left and not node.right:
                return None
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            if not node.right.left:
                node.right.left = node.left
                return node.right
            res = find_successor(node.right)
            res.left, res.right = node.left, node.right
            return res

        if not root:
            return
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            return delete(root)