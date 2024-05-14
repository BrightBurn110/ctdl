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
        
    def BSTTuanTu(self):
        def _BSTTuanTu(node):
            if node is None:
                return True
            
            # Nếu nút có cả hai nút con hoặc không có nút con nào
            if (node.left and node.right) or (node.left is None and node.right is None):
                return False

            # Kiểm tra cho các nút con
            return _BSTTuanTu(node.left) and _BSTTuanTu(node.right)

        return _BSTTuanTu(self.root)

# Sử dụng:
# Tạo cây nhị phân
tree = cayNhiPhan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)

# Kiểm tra xem cây có phải là BST tuần tự không
if tree.BSTTuanTu():
    print("Cây là cây BST tuần tự.")
else:
    print("Cây không phải là cây BST tuần tự.")