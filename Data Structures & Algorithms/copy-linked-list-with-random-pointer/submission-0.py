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
        if not head:
            return None
        o2n = {}
        curr = head
        while curr:
            cop = Node(curr.val)
            o2n[curr] = cop
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                o2n[curr].next = o2n[curr.next]
            else:
                o2n[curr].next = None
            if curr.random:
                o2n[curr].random = o2n[curr.random]
            else:
                o2n[curr].random = None
            curr = curr.next
        return o2n[head]
        