# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        if head.next == None:
            return head
        
        curr = head
        win = []
        while curr != None:
            win.insert(0, curr)
            curr = curr.next
        
        for i in range(len(win)-1):
            win[i].next = win[i+1]
        
        win[len(win)-1].next = None

        return win[0]

        