class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in range(vertices)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def SoCungVao(self, v):
        count = 0
        for vertex in range(self.vertices):
            if v in self.adj_list[vertex]:
                count += 1
        return count

# Sử dụng:
# Khởi tạo đồ thị
dt = Graph(5)
dt.add_edge(0, 1)
dt.add_edge(0, 2)
dt.add_edge(1, 2)
dt.add_edge(2, 3)
dt.add_edge(3, 0)
dt.add_edge(4, 1)
print(dt.SoCungVao(2))