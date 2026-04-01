# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        dummy = ListNode(0, head)
        beg = dummy
        curr = head
        while curr:
            start = curr
            end = curr
            for i in range(k - 1):
                end = end.next
                if not end:
                    return beg.next
            dum_next = end.next
            cur_dummy = dummy
            it = start
            for i in range(k):
                temp = it.next
                it.next = cur_dummy
                cur_dummy = it
                it = temp
            # 3->2->1  need to set dummy.next and update dummy and curr

            dummy.next = end
            start.next = dum_next
            dummy = start
            curr = dummy.next

        return beg.next


