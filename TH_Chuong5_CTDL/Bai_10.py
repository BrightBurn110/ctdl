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

    def CanBangHoanToan(self):
        def _CanBangHoanToan(node):
            if node is None:
                return True, 0

            is_left_balanced, left_height = _CanBangHoanToan(node.left)
            if not is_left_balanced:
                return False, 0

            is_right_balanced, right_height = _CanBangHoanToan(node.right)
            if not is_right_balanced:
                return False, 0
            
            if abs(left_height - right_height) > 1:
                return False, 0

            current_height = max(left_height, right_height) + 1

            return True, current_height

        balanced, _ = _CanBangHoanToan(self.root)
        return balanced

# Tạo cây nhị phân
tree = cayNhiPhan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)

# Kiểm tra cây có cân bằng hoàn toàn không
if tree.CanBangHoanToan():
    print("Cây là cây cân bằng hoàn toàn.")
else:
    print("Cây không phải là cây cân bằng hoàn toàn.")
