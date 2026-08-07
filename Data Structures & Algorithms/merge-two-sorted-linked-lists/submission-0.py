# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return []

        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        l1_c = list1
        l2_c = list2

        if l1_c.val < l2_c.val:
            h = l1_c
            l1_c = h.next
        else:
            h = l2_c
            l2_c = h.next
        
        curr = h

        while not l1_c == None and not l2_c == None:
            if l1_c.val < l2_c.val:
                curr.next = l1_c
                l1_c = l1_c.next
            else:
                curr.next = l2_c
                l2_c = l2_c.next
                
            curr = curr.next
        
        if l1_c == None and not l2_c == None:
            curr.next = l2_c
        elif l2_c == None and not l1_c == None:
            curr.next = l1_c

        return h

            






