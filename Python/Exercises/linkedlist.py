from ds import ListNode
class Node:
    def __init__(self, value):
        self.value =value
        self.next = None
    
    def __eq__(self, node):
        if isinstance(node, Node):
            return False
        return self.value == node.value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def _isEmpty(self):
        return self.head == self.tail == None
    
    def _getPreviousNode(self, node: Node):
        current = self.head
        while current.next:
            if current.next == node:
                return current.value
            current = current.next
        return None
    def addFirst(self, value: int) -> None:
        node = Node(value=value)
        if self._isEmpty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
            self.size += 1
    
    def addLast(self, value: int) -> None:
        node = Node(value=value)
        if self._isEmpty():
            self.head = self.tail = node
        else:
            prev = self.tail
            prev.next = node
            self.tail = node
            self.size += 1
    
    def removeFirst(self) -> None:
        if self._isEmpty():
            raise Exception('Linked List is empty')
        else:
            new_head = self.head.next
            self.head = new_head 
            self -= 1
    

    def removeLast(self):
        if self._isEmpty():
            raise Exception('Linked List is empty')
        else:
            previous = self._getPreviousNode(self.tail)
            previous.next = None
            self.head = previous
    
    def reverse(self):
        reversedll = LinkedList()
        current = self.head
        while current:
            reversedll.addFirst(current.value)
            current = current.next
        return reversedll

    def toArray(self) -> list:
        current = self.head
        list = []
        while current:
            print(current.value)
            list.append(current.value)
            current = current.next
        return list


ll = LinkedList()
ll.addFirst(10)
ll.addFirst(20)
ll.addFirst(30)
ll.addFirst(40)
ll.addLast(50)
ll.addLast(60)
ll.addLast(70)

k = 2 
if ll.head 
# print("reversed")
# reversed.toArray()
# ll.removeLast()
# ll.removeFirst()
# ll.removeFirst()
# ll.removeFirst()
# print("normal")
# ll.toArray()
