class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.previous = None
    def __eq__(self, obj):
        if not isinstance(obj, Node): 
            return False
        else:
            if self.key == obj.key and self.value == obj.value:
                return True

class LinkedList:
    head = Node(0,0)
    tail = Node(0,0)
    head.next = tail
    tail.previous = head
    size = 0
    def __len__(self):
        return self.size
    def __iter__(self):
        current = self.head.next
        while(current != self.tail):
            yield current.next
            current = current.next
    def addFirst(self, key: int,value: int) -> None:
        node = Node(key=key, value=value)
        node.next = self.head.next
        self.head.next.previous = node
        self.head.next = node
        self.size +=1

    def addLast(self, key: int,value: int) -> None:
        node = Node(key=key, value=value)
        node.previous = self.tail.previous
        node.next = self.tail
        self.tail.previous.next = node
        self.tail.previous = node
        self.size +=1

    def removeLast(self) -> None:
        old_last = self.tail.previous
        new_last = old_last.previous
        new_last.next = self.tail
        self.tail.previous = new_last
        self.size -= 1

    def removeFirst(self) -> None:
        old_first = self.head.next
        new_first = old_first.next
        new_first.previous = self.head
        self.head.next = new_first

    def toArray(self) -> list:
        result = []
        current = self.head.next
        while (current != Node(0,0)):
            if isinstance(current, Node):
                result.append((current.key, current.value))
                current = current.next
        return result
    
class HashTables():
    list = []
    def __init__(self, size: int):
        self.size = size
    
    def __hash(self,key: int) -> int:
        return key % self.size 
    
    def put(self, key: int, value: int) -> None:
        index = self.__hash(key=key)
        ll = LinkedList()
        if self.list and len(self.list) > index:
            ll = self.list[index]
            if isinstance(ll, LinkedList):
                # ll.addLast(key=key, value=value)
                for element in ll:
                    if element.key == key:
                        element.value = value
                        return
                ll.addLast(key=key, value=value)
        else:
            ll.addLast(key=key, value=value)
            self.list.append(ll)
            
    def get(self, key: int) -> int:
        index = self.__hash(key)
        if len(self.list) == 0 or index > len(self.list): 
            return None
        ll = self.list[index]
        for element in ll:
            if element.key == key:
                return element.value
        return None
