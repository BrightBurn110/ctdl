class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in range(vertices)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def SoCungRa(self, v):  # Phương thức tính số cung ra khỏi đỉnh v trong đồ thị
        if v not in self.adj_list:
            return 0
        return len(self.adj_list[v])

# Sử dụng:
# Khởi tạo đồ thị
dt = Graph(5)
dt.add_edge(0, 1)
dt.add_edge(0, 2)
dt.add_edge(1, 2)
dt.add_edge(2, 3)
dt.add_edge(3, 0)
dt.add_edge(4, 1)
print(dt.SoCungRa(2))