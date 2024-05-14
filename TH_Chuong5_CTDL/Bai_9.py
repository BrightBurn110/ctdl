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
    def CayCon(self, cay2):
        if self.root is None or cay2.root is None:
            return False
        return self.SoSanhNode(self.root, cay2.root) or self.CayConNode(self.root.left, cay2) or self.CayConNode(self.root.right, cay2)

    def CayConNode(self, node, cay2):
        if node is None:
            return False
        if self.SoSanhNode(node, cay2.root):
            return True
        return self.CayConNode(node.left, cay2) or self.CayConNode(node.right, cay2)

#Ex:
cay = cayNhiPhan()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)

cay1 = cayNhiPhan()
cay1.root = Node(1)
cay1.root.left = Node(2)
cay1.root.right = Node(3)

cay2 = cayNhiPhan()
cay2.root = Node(2)
cay2.root.left = Node(4)
cay2.root.right = Node(5)

print("cay2 là cây con của cay1:", cay1.CayCon(cay2))