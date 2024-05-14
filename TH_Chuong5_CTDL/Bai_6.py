class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
    
class cayNhiPhan:
    def __init__(self):
        self.root = None
    def soNut(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.soNut(node.left) + self.soNut(node.right)

        return new_tree
    def kiemTraAVL(self, node):
        if node is None:
            return True
        if abs(self.chieuCao(node.left) - self.chieuCao(node.right)) >1:
            return False
        
        return self.kiemTraAVL(node.left) and self.kiemTraAVL(node.right)

#Ex:
cay = cayNhiPhan()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)
print("Cây là AVL:", cay.kiemTraAVL(cay.root))