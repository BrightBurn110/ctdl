from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in range(vertices)}
    def add_edge(self, u, v):
        # Thêm cạnh (u, v) vào danh sách kề
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def bfs(self, start_vertex, visited):
        # Khởi tạo hàng đợi và thêm đỉnh xuất phát vào hàng đợi
        queue = deque()
        queue.append(start_vertex)
        # Đánh dấu đỉnh xuất phát đã được thăm
        visited.add(start_vertex)
        
        # Duyệt qua các đỉnh kề của đỉnh hiện tại
        while queue:
            current_vertex = queue.popleft()
            for neighbor in self.adj_list[current_vertex]:
                # Nếu đỉnh kề chưa được thăm, thêm vào hàng đợi và đánh dấu đã thăm
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def SoThanhPhan(self):  # Phương thức tính số lượng thành phần liên thông
        visited = set()  # Danh sách các đỉnh đã được thăm
        components = 0   # Biến đếm số lượng thành phần liên thông

        # Duyệt qua tất cả các đỉnh của đồ thị
        for vertex in range(self.vertices):
            # Nếu đỉnh chưa được thăm, thực hiện BFS để thăm tất cả các đỉnh trong thành phần liên thông này
            if vertex not in visited:
                self.bfs(vertex, visited)
                components += 1  # Tăng biến đếm thành phần lên 1 sau khi duyệt xong một thành phần liên thông

        return components

# Sử dụng:
# Khởi tạo đồ thị
dt = Graph(7)
dt.add_edge(0, 1)
dt.add_edge(0, 2)
dt.add_edge(1, 2)
dt.add_edge(3, 4)
dt.add_edge(5, 6)
print(dt.SoThanhPhan())