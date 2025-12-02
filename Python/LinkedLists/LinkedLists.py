class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList():
    size = 0
    first = None
    last = None
    def isEmpty(self):
        return self.first == None
    ## O(1)
    def addLast(self, item):
        node = Node(item)
        if self.isEmpty():
            self.first = self.last = node
            self.size += 1
        else:
            self.last.next = node
            self.last = node
            self.size += 1
    ## O(1)
    def addFirst(self, item):
        node = Node(item)
        if self.isEmpty():
            self.first =self.last = node
            self.size += 1
        else:
            node.next = self.first
            self.first = node
            self.size += 1
    ## O(n)
    def indexOf(self, item):
        current = self.first
        index = 0 
        if self.isEmpty():
            return -1
        while current != None:
            if current.value == item:
                return index
            else:
                index += 1
                current = current.next
        return -1
    ## O(1)
    def removeFirst(self):
        if self.isEmpty():
            raise IndexError
        elif self.first == self.last:
            self.first = self.last = None
        else:
            newFirst = self.first.next
            self.first = None
            self.first = newFirst
        self.size -=1
    ## O(n)
    def getPrevious(self, item):
        current = self.first
        while current != None:
            if current.next == item:
                return current
            current = current.next
        # return None
    ## O(n)
    def removeLast(self):
        if self.isEmpty():
            return IndexError
        elif self.first == self.last:
            self.first = self.last = None
        else:
            previous = self.getPrevious(self.last)
            self.last = previous
            self.last.next = None
        self.size-=1
    ## O(n)
    def toList(self):
        list = []
        current = self.first
        while current != None:
            list.append(current.value)
            current = current.next
        return list
    ## O(1)
    def length(self):
        return self.size
    ## O(n)
    def reverse(self):
        if self.isEmpty():
            return None
        previous = self.first
        current = self.first.next
        while current != None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.last = self.first
        self.last.next = None
        self.first = previous

    def reverseNewList(self):
        reversedLinkedList = LinkedList()
        reversedList = []
        current = self.last
        for i in range(0,self.size):
            previous = self.getPrevious(current)
            if previous == None:
                reversedLinkedList.addLast(current.value)
                reversedList.append(current.value)
                break
            else:
                reversedLinkedList.addLast(current.value   )
                reversedList.append(current.value)
            current = previous
        return reversedLinkedList
    
    def findKthFromEnd(self, k):
        if (self.isEmpty() | self.size == k | self.size < k):
            raise ValueError
        else:
            p1 = p2 = self.first
            for i in range(0, k-1):
                # p1 = p1.next
                p2 = p2.next
            while(p2 != self.last):
                p1 = p1.next
                p2 = p2.next
            return p1.value
        
    def findMiddle(self):
        if self.isEmpty():
            raise ValueError
        fp = sp = self.first
        while(sp != self.last and sp.next != self.last):
            fp = fp.next
            sp = sp.next.next
        if (sp == self.last):
            return fp.value
        else:
            return ','.join((str(fp.value), str(fp.next.value)))
        return fp.value

    # def addFist(self, item):

    # def indexOf(self, item): d d