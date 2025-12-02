class DoulyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = {}
        self.head = DoulyLinkedListNode(0,0)
        self.tail = DoulyLinkedListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # def get(self, key: int) -> object:
    def put(self, key: int, value: int) -> None:
        if len(self.hashmap) > self.capacity:
            # self.remove_node(self.hashmap[self.hashmap.head.next.key])
            del self.hashmap[self.hashmap.head.next.key]
            self.remove_node(self.hashmap.head.next)
        node = DoulyLinkedListNode(key=key, value=value)
        self.hashmap[key] = node
        self.add_to_tail(node=node)


    def add_to_tail(self, node: DoulyLinkedListNode) -> None:
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        prev_node.next = node
        self.tail.prev = node
    
    def remove_node(self, node: DoulyLinkedListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev