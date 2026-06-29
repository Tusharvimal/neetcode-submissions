# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        ind = length - n
        if(ind == 0):
            return head.next

        count = 0
        temp = head
        while count<ind - 1:
            count+=1
            temp = temp.next
        print(temp.val)
        if (temp.next.next):
            temp.next = temp.next.next
        else:
            temp.next = None

        return head
        