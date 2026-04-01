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
        visit = deque([])
        visit.append(node)
        while visit:
            curr = visit.popleft()
            if curr not in oldToNew:
                oldToNew[curr] = Node(curr.val, [])
            for n in curr.neighbors:
                if n in oldToNew:
                    oldToNew[curr].neighbors.append(oldToNew[n])
                else:
                    oldToNew[n] = Node(n.val, [])
                    oldToNew[curr].neighbors.append(oldToNew[n])
                    visit.append(n)
        return oldToNew[node]


        
            