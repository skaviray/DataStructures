# create a binary tree
import math
class Node():
    def __init__(self,value: int):
        self.value = value
        self.right = None
        self.left = None
    
    def __float__(self):
        return float(self.value)

class BinaryTree():
    root = None
    def put(self, item: int):
        node = Node(item)
        if self.root == None:
            self.root = node
        else:
            current = self.root
            while(True):
                if current.value > item:
                    if current.left == None:
                        current.left = node
                        return
                    current = current.left
                else:
                    if current.right == None:
                        current.right = node
                        return 
                    current = current.right
    
    def get(self, item: int) -> bool:
        if self.root == None:
            return False
        else:
            current = self.root
            while(current != None):
                if current.value  and current.value > item:
                    if current.left.value == item:
                        return True
                    current = current.left
                else:
                    if current.right and current.right.value == item:
                        return True
                    current = current.left
            return False
            
    def preOrderedTraverse(self, root):
        if root == None:
            return
        print(root.value)
        self.preOrderedTraverse(root.left)
        self.preOrderedTraverse(root.right)

    def inOrderedTraverse(self, root):
        if root == None:
            return
        self.postOrderedTraverse(root.left)
        print(root.value)
        self.postOrderedTraverse(root.right)
    def postOrderedTraverse(self, root):
        if root == None:
            return
        self.postOrderedTraverse(root.left)
        self.postOrderedTraverse(root.right)
        print(root.value)
    
    def height(self, root) -> int:
        if root == None:
            return -1
        return max(self.height(root.left), self.height(root.right)) +  1 
    
    def isBinaryTree(self) -> bool:
        return self.validate(self.root, +math.inf, -math.inf)

    def validate(self,root,  upper, lower) -> bool:
        if root == None:
            return True
        return float(lower) < float(root) < float(upper) and \
        self.validate(root.left,root, -math.inf) and \
        self.validate(root.right, +math.inf, root)