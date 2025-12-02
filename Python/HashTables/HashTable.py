class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    def __len__(self):
        return self.size
    
    def __iter__(self):
        current = self.first
        while current:
            yield current.next
            current = current.next

    def isEmpty(self):
        return self.first == self.last == None

    def getPrevious(self, item):
        current = self.first
        while(current):
            if isinstance(item,Node):
              if current.next == item:
                return current
            else:
                if current.next.value == item:
                    return current
            current = current.next
        return None

    def getNext(self, item):
        current = self.first
        while(current):
            if isinstance(item,Node):
              if current == item:
                return current
            else:
                if current.value == item:
                    return current
            current = current.next
        return None

    
    def addFirst(self, item):
        node = Node(item)
        if self.isEmpty():
            self.first = self.last = node
        else:
            nextNode = self.first
            node.next = nextNode
            self.first = node
        self.size += 1

    def addLast(self, item):
        node = Node(item)
        if self.isEmpty():
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1
    
    def removeFirst(self):
        if self.isEmpty():
            raise ValueError("Invalid operation on an empty Linked List")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
        self.size -= 1
    
    def removeLast(self):
        if self.isEmpty():
            raise ValueError("Invalid operation on an empty Linked List")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            previous = self.getPrevious(self.last)
            previous.next = None
            self.last = previous
        self.size -= 1
    
    def remove(self, item):
        if self.isEmpty():
            raise ValueError("Invalid operation on an empty Linked List")
        elif self.first == self.last == item:
            self.first = self.last = None 
        else:
            previous = self.getPrevious(item)
            next = self.getNext(item)
            print(previous, next)
            if previous and next:
                print(item)
                previous.next = next.next
                self.size -= 1

    def toArray(self):
        current = self.first
        list = []
        while(current != None):
            list.append(current.value)
            current = current.next
        return list

class Entry():
    def __init__(self, key,value):
        self.key = key
        self.value = value

class HashTable():
    def __init__(self, size):
        self.table = []
        self.size = size
    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        item = Entry(key,value)
        index = self.hash(key)
        if self.table and len(self.table) > index:
            if self.table[index] and isinstance(self.table[index], LinkedList):
                linkedList = self.table[index]
                for element in linkedList:
                    if isinstance(element, Node):
                        node = element.value
                        if isinstance(node, Entry) and node.key == key:
                            node.value = value
                            return       
                linkedList.addLast(item)
        else:
            linkedList = LinkedList()
            linkedList.addFirst(item)
            self.table.append(linkedList)

    def get(self, key):
        index = self.hash(key)
        if self.table and self.table[index]:
            linkedList = self.table[index]
            if isinstance(linkedList, LinkedList):
                for element in linkedList:
                    if isinstance(element, Node):
                        node = element.value
                        if isinstance(node, Entry) and node.key == key:
                            return node.value
                return None
        else:
            return None
    def remove(self,key):
        index = self.hash(key)
        if self.table and self.table[index]:
            linkedList = self.table[index]
            if isinstance(linkedList, LinkedList):
                for element in linkedList:
                    if isinstance(element, Node):
                        if element.value.key == key:
                            print("found")
                            linkedList.remove(element)
                            return
                raise Exception(f"Key {0} not found")
        else:
            raise Exception(f"Key {0} not found")

    def toArray(self):
        for i in self.table:
            print(i.length())
        # print(self.table)

# list = LinkedList()
# list.addFirst(10)
# list.addFirst(20)
# list.addLast(30)
# list.addLast(40)
# list.addFirst(50)
# list.remove(30)
# # list.removeLast()
# print(list.toArray())

hashTable = HashTable(10)
for i in range(0,1000):
    hashTable.put(i, 20)
hashTable.put(100, 200)
hashTable.put(101, 300)
hashTable.put(102, 400)
hashTable.remove(101)
for i in hashTable.table:
    if isinstance(i, LinkedList):
        print(len(i))
print(hashTable.get(100))