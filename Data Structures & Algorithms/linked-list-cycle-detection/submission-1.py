# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        curr = head

        while curr != None:
            if visited.get(curr):
                return True
            visited[curr] = True
            curr = curr.next

        return False
        