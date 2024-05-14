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
    def soNutLa(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        else:
            return self.soNutLa(node.left) + self.soNutLa(node.right)

#Ex:
cay = cayNhiPhan()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)
print("Số nút lá của cây:", cay.soNutLa(cay.root))