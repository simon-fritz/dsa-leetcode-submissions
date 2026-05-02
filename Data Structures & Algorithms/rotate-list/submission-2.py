# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        #count list:
        p = head
        count = 0
        while p:
            count += 1
            p = p.next
        true_k = k % count
        if true_k == 0:
            return head
        p = head
        new_head = None
        for i in range(count-true_k-1):
            p = p.next
        new_head = p.next
        p.next = None
        p = new_head
        while p and p.next:
            p = p.next
        p.next = head
        return new_head


