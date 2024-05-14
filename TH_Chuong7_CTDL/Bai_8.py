from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in range(vertices)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def has_path(self, start_vertex, end_vertex):
        visited = set()
        queue = deque()
        queue.append(start_vertex)
        visited.add(start_vertex)

        while queue:
            current_vertex = queue.popleft()
            if current_vertex == end_vertex:
                return True
            for neighbor in self.adj_list[current_vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return False

    def DuongDi(self, v1, v2):  # Phương thức kiểm tra xem có đường đi từ v1 đến v2 hay không
        return self.has_path(v1, v2)

# Sử dụng:
# Khởi tạo đồ thị
dt = Graph(5)
dt.add_edge(0, 1)
dt.add_edge(0, 2)
dt.add_edge(1, 2)
dt.add_edge(2, 3)
print(dt.DuongDi(0, 3))
print(dt.DuongDi(3, 4))