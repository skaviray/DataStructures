class Node:
    def __init__(self, value: str):
        self.value = value
        self.children = {}
        self.isEndOfWord = False
    def __str__(self):
        return self.value + ''.join(self.children)
    
    def hasChildren(self, item):
        if isinstance(self.children, dict):
            if self.children.get(item):
                return True
        if isinstance(self.children, list):
            index = ord(item) - ord('a')
            if self.children[index]:
                return True
        return False
    
    def getChildren(self,item):
        if isinstance(self.children, dict):
            return self.children.get(item)
        if isinstance(self.children, list):
            index = ord(item) - ord('a')
            return self.children[index]
        return False 
    
    def getChildrens(self):
        if isinstance(self.children, dict):
            return self.children.values()  
class Trie():
    root = Node("")
    
    def insert(self,value: str):
        current = self.root
        for char in value:
            # index = ord(char) - ord('a')
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]
        current.isEndOfWord = True
    
    def contains(self, value: str) -> bool:
        if not value:
            return False
        current = self.root
        for char in value:
            if current.hasChildren(char):
                current = current.getChildren(char)
            else:
                return False
        return current.isEndOfWord
    
    def preOrderTreversal(self, root: Node):
        print(root.value)
        for element in root.getChildrens():
            self.preOrderTreversal(element)

    def remove(self, s: str):
        self.__remove(self.root, s, 0)
    def __remove(self,root: Node, s: str, index: int ):
        if index == len(s):
            return 
        ch = s[index]
        # index = index + 1
        child = root.getChildren(ch)
        if child == None:
            return
        self.__remove(child, s, index + 1)
        print(root.value)
    # def postOrderTreversal(self, root: Node, item: str):
    #     for element in root.getChildrens():
    #         self.postOrderTreversal(element)
    #     print(root.value)
    
    # def remove(self,root, string, index):
    #     start = s[0]
    #     end = s[1]
    #     if not self.root.hasChildren(start):
    #         return False
    #     root = self.root.getChildren(start)
    #     self.postOrderTreversal(root, end)


trie = Trie()
trie.insert("cannada")
trie.insert("can")
# trie.postOrderTreversal(trie.root)
trie.remove("can")
print("hello")