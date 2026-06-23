# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None):
            return head
        curr = head
        prev = None
        t = curr.next

        while (t!=None):
            prev = curr
            curr = t
            t = t.next
            curr.next = prev

        head.next = None
        return curr
