# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return 
        dummy = ListNode(0)
        curr = dummy
        n_lists = len(lists)

        none_counter = 0

        while none_counter < n_lists:
            none_counter = 0
            mini = float('inf')
            min_ind = 0
            for i in range(n_lists):
                if not lists[i]:
                    none_counter+=1
                    continue
                temp_head = lists[i]
                if temp_head.val < mini:
                    mini = temp_head.val
                    min_ind = i
            temp_prev = lists[min_ind]
            if temp_prev:
                lists[min_ind] = lists[min_ind].next
                temp_prev.next = None
            curr.next = temp_prev
            curr = curr.next
            mini = 0
            min_ind = 0

        return dummy.next
        