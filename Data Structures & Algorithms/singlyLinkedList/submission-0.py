class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        # Dummy head node makes removal from index 0 easier
        self.head = ListNode(-1)
        self.tail = self.head   # tail always points to the last real node

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        # If list was empty, update tail
        if new_node.next is None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        # Start at dummy head to get predecessor of the target node
        curr = self.head
        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1
        # curr is the node before the target (or None if index too large)
        if curr and curr.next:
            # If removing the tail, update tail
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> list[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res