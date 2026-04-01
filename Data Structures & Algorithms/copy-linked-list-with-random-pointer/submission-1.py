"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}
        dummy = Node(0)
        res = dummy

        curr = head
        while curr:
            if curr in oldToNew:
                print(curr.val)
                currNode = oldToNew[curr]
            else:
                currNode = Node(curr.val)
                oldToNew[curr] = currNode
            if not curr.next: 
                currNode.next = None
            else:
                if curr.next in oldToNew:
                    currNode.next = oldToNew[curr.next]
                else:
                    currNode.next = Node(curr.next.val)
                    oldToNew[curr.next] = currNode.next
            if not curr.random: 
                currNode.random = None
            else:
                if curr.random in oldToNew:
                    currNode.random = oldToNew[curr.random]
                else:
                    currNode.random = Node(curr.random.val)
                    oldToNew[curr.random] = currNode.random
            dummy.next = currNode
            dummy = dummy.next
            curr = curr.next

        return res.next

        
            