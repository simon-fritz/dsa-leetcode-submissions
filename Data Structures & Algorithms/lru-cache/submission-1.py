class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.listmap = {}

        self.start, self.end = Node(0,0), Node(0,0)
        self.end.prev = self.start
        self.start.next = self.end
    
    def insert(self,node):
        tmp = self.end.prev
        tmp.next = node
        node.next = self.end
        self.end.prev = node
        node.prev = tmp

    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if not key in self.listmap:
            return -1
        # remove node from linked list
        node = self.listmap[key]
        self.remove(node)
        # insert at end
        self.insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.listmap:
            self.remove(self.listmap[key])
        self.listmap[key] = Node(key,value)
        self.insert(self.listmap[key])

        if len(self.listmap) > self.capacity:
            lru = self.start.next
            self.remove(lru)
            del self.listmap[lru.key]

            
        
