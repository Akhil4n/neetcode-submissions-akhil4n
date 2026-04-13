# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge(n1, n2):
            dummy = ListNode()
            curr = dummy
            while n1 and n2:
                if n1.val <= n2.val:
                    curr.next = n1
                    n1 = n1.next
                    curr = curr.next
                else:
                    curr.next = n2
                    n2 = n2.next
                    curr = curr.next
            if n1:
                curr.next = n1
            if n2:
                curr.next = n2
            return dummy.next
        
        while len(lists) > 1:
            n1 = lists.pop()
            n2 = lists.pop()
            mn = merge(n1, n2)
            lists.insert(0, mn)
            
        return lists[0]

