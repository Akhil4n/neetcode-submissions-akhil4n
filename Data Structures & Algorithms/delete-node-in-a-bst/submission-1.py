# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def get_successor(node):
            while node.left:
                node = node.left
            return node
        def delete(curr, key):
            if not curr:
                return None
            if key < curr.val:
                curr.left = delete(curr.left, key)
            elif key > curr.val:
                curr.right = delete(curr.right, key)
            else:
                if not curr.left and not curr.right:
                    return None
                if curr.left and curr.right:
                    curr.val = get_successor(curr.right).val
                    curr.right = delete(curr.right, curr.val)
                    return curr
                if curr.left:
                    return curr.left
                else:
                    return curr.right

            return curr

        return delete(root, key)


