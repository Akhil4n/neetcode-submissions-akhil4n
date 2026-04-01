# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        l, r = list1, list2
        while l and r:
            lV = l.val
            rV = r.val
            if lV < rV:
                curr.next = l
                l = l.next
                curr = curr.next
            else:
                curr.next = r
                r = r.next
                curr = curr.next
        while l:
            curr.next = l
            l = l.next
            curr = curr.next
        while r:
            curr.next = r
            r = r.next
            curr = curr.next
        return dummy.next

        