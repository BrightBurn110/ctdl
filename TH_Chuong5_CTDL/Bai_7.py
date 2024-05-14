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
    
    def chepNode(self, node):
        if node is None:
            return None
        new_node = Node(node.info)
        new_node.left = self.chepNode(node.left)
        new_node.right = self.chepNode(node.right)
        return new_node
    
    def chep(self):
        if self.root is None:
            return None
        new_tree = cayNhiPhan()
        new_tree.root = self.chepNode(self.root)
        return new_tree  # Trả về cây sao chép

# Tạo cây nhị phân
cay = cayNhiPhan()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)

# Sao chép cây nhị phân
cay_sao_chep = cay.chep()

# Hiển thị kết quả của cây sao chép
print("Kết quả của cây sao chép:")
print("Nút gốc:", cay_sao_chep.root.info)
if cay_sao_chep.root.left:
    print("Cây con bên trái của nút gốc:", cay_sao_chep.root.left.info)
else:
    print("Cây con bên trái của nút gốc: None")

if cay_sao_chep.root.right:
    print("Cây con bên phải của nút gốc:", cay_sao_chep.root.right.info)
else:
    print("Cây con bên phải của nút gốc: None")

if cay_sao_chep.root.left:
    if cay_sao_chep.root.left.left:
        print("Cây con bên trái của nút gốc của cây con bên trái:", cay_sao_chep.root.left.left.info)
    else:
        print("Cây con bên trái của nút gốc của cây con bên trái: None")

    if cay_sao_chep.root.left.right:
        print("Cây con bên phải của nút gốc của cây con bên trái:", cay_sao_chep.root.left.right.info)
    else:
        print("Cây con bên phải của nút gốc của cây con bên trái: None")
else:
    print("Cây con bên trái của nút gốc không tồn tại.")
