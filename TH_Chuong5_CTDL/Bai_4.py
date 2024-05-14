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
    def soNutTrungGian(self, node):
        if node is None or (node.left is None and node.right is None):
            return 0
        else:
            count_left = self.soNutTrungGian(node.left)
            count_right = self.soNutTrungGian(node.right)
            if node.left is not None and node.right is not None:
                return count_left + count_right + 1
            else:
                return count_left + count_right

#Ex:
cay = cayNhiPhan()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)
print("Số nút trung gian của cây:", cay.soNutTrungGian(cay.root))