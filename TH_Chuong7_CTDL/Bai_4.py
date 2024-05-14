class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in range(vertices)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def ChuaDinh(self, v):  # Phương thức kiểm tra xem đỉnh v có tồn tại trong đồ thị hay không
        if v in self.adj_list:
            return True
        else:
            return False

# Sử dụng:
# Khởi tạo đồ thị
dt = Graph(5)
dt.add_edge(0, 1)
dt.add_edge(0, 2)
dt.add_edge(1, 2)
dt.add_edge(2, 3)
print(dt.ChuaDinh(2))
print(dt.ChuaDinh(5))