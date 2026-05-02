"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        randoms = {}
        dummy = Node(0,None)
        cur = head
        clone_cur = dummy
        while cur:
            clone_cur.next = Node(cur.val,None,None)
            randoms[cur] = clone_cur.next
            clone_cur = clone_cur.next
            cur = cur.next
        cur = head
        clone_cur = dummy.next
        while cur:
            if cur.random:
                clone_cur.random = randoms[cur.random]
            clone_cur = clone_cur.next
            cur = cur.next
        return dummy.next
        
        
