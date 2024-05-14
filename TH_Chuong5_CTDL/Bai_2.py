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
    def chieuCao(self, node):
        if node is None:
            return -1
        else:
            left_height = self.chieuCao(node.left)
            right_height = self.chieuCao(node.right)
            return max(left_height, right_height) + 1
    def chieuCaoCay(self):
        return self.chieuCao(self.root)

#Ex:
cay = cayNhiPhan()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)

print("Chiều cao của cây:", cay.chieuCaoCay())