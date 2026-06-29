# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        mid = length // 2
        count = 0
        temp = head
        last = None
        print(mid)
        while count<mid:
            count+=1
            last = temp
            temp = temp.next

        ## reverse
        last.next = None
        prev = None
        curr = temp
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head2 = prev
        head1 = head.next
        temp = head

        while head2:
            temp.next = head2
            head2 = head2.next
            temp = temp.next
            if (head1):
                temp.next = head1
                head1 = head1.next
                temp = temp.next
        