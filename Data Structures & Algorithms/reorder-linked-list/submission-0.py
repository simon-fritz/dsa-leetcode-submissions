# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # 1. Find the middle using slow/fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Split the list (slow is at middle)
        second = slow.next
        slow.next = None  # Cut off the first half
        
        # 3. Reverse the second half
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # 4. Merge the two halves
        first = head
        second = prev  # prev is now head of reversed second half
        
        while second:
            # Save next pointers
            temp1 = first.next
            temp2 = second.next
            
            # Reorder
            first.next = second
            second.next = temp1
            
            # Move pointers forward
            first = temp1
            second = temp2
