class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in range(vertices)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def has_cycle_util(self, vertex, visited, rec_stack):
        visited[vertex] = True
        rec_stack[vertex] = True

        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                if self.has_cycle_util(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[vertex] = False
        return False

    def ChuTrinh(self):
        visited = [False] * self.vertices
        rec_stack = [False] * self.vertices

        for vertex in range(self.vertices):
            if not visited[vertex]:
                if self.has_cycle_util(vertex, visited, rec_stack):
                    return True

        return False

#Ex:
# Khởi tạo đồ thị
dt = Graph(5)
dt.add_edge(0, 1)
dt.add_edge(0, 2)
dt.add_edge(1, 2)
dt.add_edge(2, 0)
dt.add_edge(2, 3)
print('Bai 3')
print(dt.ChuTrinh())
