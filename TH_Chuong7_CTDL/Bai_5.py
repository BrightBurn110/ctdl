class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in range(vertices)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def BacDinh(self, v):  # Phương thức tính bậc của đỉnh v trong đồ thị
        return len(self.adj_list[v])

# Sử dụng:
# Khởi tạo đồ thị
dt = Graph(5)
dt.add_edge(0, 1)
dt.add_edge(0, 2)
dt.add_edge(1, 2)
dt.add_edge(2, 3)
print(dt.BacDinh(2))