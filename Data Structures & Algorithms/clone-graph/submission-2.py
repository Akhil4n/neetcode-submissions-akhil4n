"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}
        visit = deque()
        visit.append(node)
        while visit:
            curr = visit.popleft()
            if curr.val not in oldToNew:
                oldToNew[curr.val] = Node(curr.val, [])
            for n in curr.neighbors:
                if n.val in oldToNew:
                    oldToNew[curr.val].neighbors.append(oldToNew[n.val])
                else:
                    oldToNew[n.val] = Node(n.val, [])
                    oldToNew[curr.val].neighbors.append(oldToNew[n.val])
                    visit.append(n)
        return oldToNew[node.val]


        
            