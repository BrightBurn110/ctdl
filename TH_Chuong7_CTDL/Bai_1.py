from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Thêm một cạnh vào đồ thị
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Hàm đệ quy để kiểm tra đồ thị liên thông
    def _DFSUtil(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self._DFSUtil(i, visited)

    # Kiểm tra đồ thị liên thông
    def LienThong(self):
        # Kiểm tra đồ thị rỗng
        if len(self.graph) == 0:
            return False

        # Khởi tạo visited dictionary để đánh dấu các đỉnh đã được duyệt
        visited = {v: False for v in self.graph}

        # Sử dụng DFS để duyệt đồ thị từ một đỉnh bất kỳ
        self._DFSUtil(next(iter(self.graph)), visited)

        # Kiểm tra xem tất cả các đỉnh đã được duyệt hay không
        for vertex in visited:
            if not visited[vertex]:
                return False

        return True

#Ex:

dt = Graph()
dt.add_edge(0, 1)
dt.add_edge(0, 2)
dt.add_edge(1, 2)
dt.add_edge(3, 4)
print(dt.LienThong())
dt.add_edge(2, 3)
print(dt.LienThong())