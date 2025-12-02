import math
input = [10,5,15,6,1,8,12,18,17]
input2 =[10,5,15,6,1,8,12,18,17]
# Always left < node < right

class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    def __float__(self):
        return float(self.value)

class BinaryTree():
    def __init__(self):
        self.root = None
    
    def __eq__(self, tree):
        if not isinstance(tree, BinaryTree):
            return False
        if self.height(self.root) != tree.height(tree.root):
            return False
        return self.__equals(self.root, tree.root)

    def __equals(self, first: Node, second: Node):
        if first == second == None:
            return True
        if first != None and second != None:
            return first.value == second.value \
                   and self.__equals(first.left, second.left) \
                   and self.__equals(first.right, second.right)
        return False
    
    def swapRoot(self):
        temp = self.root.left
        self.root.left = self.root.right
        self.root.right = temp
    # def checkNodes(self, parent, node):
    def push(self, item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        else:
            parent = self.root
            # if self.root.value > item:           
            while(True):
                if parent.value > item:
                    if parent.left == None:
                        parent.left = node
                        return
                    parent = parent.left
                else:
                    if parent.right == None:
                        parent.right = node
                        return
                    parent = parent.right
    def find(self, item):
        current = self.root
        while (current != None):
            if item < current.value:
                current = current.left
            elif item > current.value:
                current = current.right
        return False
    
    def traversePreOrder(self,root: Node  ): 
        if root == None:
            return
        print(root.value)
        self.traversePreOrder(root.left)
        self.traversePreOrder(root.right)

    def traverseInOrder(self,root: Node  ): 
        if root == None:
            return
        self.traverseInOrder(root.left)
        print(root.value)
        self.traverseInOrder(root.right)           

    def traversePostOrder(self,root: Node  ): 
        if root == None:
            return
        self.traversePostOrder(root.left)
        self.traversePostOrder(root.right) 
        print(root.value) 
    
    def height(self, root: Node):
        if root == None:
            return -1
        # if root.left == None and root.right == None:
        #     return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def isBinaryTree(self, root: Node, upperlimit, lowerlimit):
        if root == None:
            return True
        return float(lowerlimit) < float(root) < float(upperlimit) and \
        self.isBinaryTree(root.left,root, -math.inf) \
        and self.isBinaryTree(root.right, +math.inf, root)
        
binaryTree1 = BinaryTree()
binaryTree2 = BinaryTree()
for i in input:
    binaryTree1.push(i)
    binaryTree2.push(i)
# for i in input2:
#     binaryTree2.push(i)

# print(binaryTree1 == binaryTree2)
binaryTree1.swapRoot()
print(binaryTree1.isBinaryTree(binaryTree1.root, math.inf, -math.inf))
# print(binaryTree.find(100))
# binaryTree.traversePostOrder(binaryTree.root)
# print(binaryTree1.height(binaryTree1.root))
# print(binaryTree2.height(binaryTree2.root))
