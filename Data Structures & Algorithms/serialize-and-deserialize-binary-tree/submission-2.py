# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder(node):
            if not node:
                res.append("n")
                return

            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        chars = data.split(',')
        self.i = 0
        def parse(i):
            if chars[i] == 'n':
                self.i += 1
                return None
            node = TreeNode(int(chars[i]))
            self.i += 1
            node.left = parse(self.i)
            node.right = parse(self.i)
            return node
        return parse(0)

            











