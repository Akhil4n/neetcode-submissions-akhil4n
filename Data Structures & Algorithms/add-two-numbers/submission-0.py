# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ""
        n2 = ""
        h1 = l1
        h2 = l2
        while h1:
            n1 = str(h1.val) + n1
            h1 = h1.next
        while h2:
            n2 = str(h2.val) + n2
            h2 = h2.next
        res = str(int(n1) + int(n2))
        if len(res) == 1:
            return ListNode(int(res))
        rH = ListNode(int(res[-1]))
        curr = rH
        for i in range(len(res) - 2, -1, -1):
            key = int(res[i])
            curr.next = ListNode(key)
            curr = curr.next
        return rH

