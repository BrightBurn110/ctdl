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

    def kiemTraBST(self, node, min_val = float('-inf'), max_val = float('-inf')):
        if node is None:
            return True
        if node.info <= min_val or node.info >= max_val:
            return False
        return (self.kiemTraBST(node.left, min_val, node.info) and 
                self.kiemTraBST(node.right, max_val, node.info))
    
#Ex:
cay = cayNhiPhan()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)
print("Cây là BST: ", cay.kiemTraBST(cay.root))