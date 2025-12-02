class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.next = None
        self.previous = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.previous = self.head
    
    def __add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.previous = node
        self.head.next = node
    
    def __remove(self, node):
        prev = node.previous
        next = node.next
        prev.next = next
        next.previous  = prev 
