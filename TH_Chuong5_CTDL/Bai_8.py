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
    def SoSanhNode(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return (node1.info == node2.info and
                self.SoSanhNode(node1.left, node2.left) and
                self.SoSanhNode(node1.right, node2.right))

    def SoSanh(self, cay2):
        return self.SoSanhNode(self.root, cay2.root) if self.root is not None else cay2.root is None

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
cay2.root = Node(1)
cay2.root.left = Node(2)
cay2.root.right = Node(3)

print("Hai cây giống nhau:", cay1.SoSanh(cay2))