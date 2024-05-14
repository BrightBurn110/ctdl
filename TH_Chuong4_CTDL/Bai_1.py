class Node:
    def __init__(self, data):
        self.Info = data
        self.Next = None
class DSLK:
    def __init__(self):
        self.Head = None
    def Them(self, data):
        new_node = Node(data)
        if self.Head is None:
            self.Head = new_node
            return
        last = self.Head
        while last.Next:
            last = last.Next
        last.Next = new_node
    def InNguoc_DeQui(self, node):
        if node is None:
            return
        self.InNguoc_DeQui(node.Next)
        print(node.Info, end=" ")
    def InNguoc_KhongDeQui(self):
        stack = []
        current = self.Head
        while current:
            stack.append(current)
            current = current.Next
        while stack:
            node = stack.pop()
            print(node.Info, end=" ")

if __name__ == "__main__":
    dslk = DSLK()
    dslk.Them(1)
    dslk.Them(2)
    dslk.Them(3)
    dslk.Them(4)

    print("In ngược danh sách liên kết (sử dụng đệ qui):")
    dslk.InNguoc_DeQui(dslk.Head)

    print("\nIn ngược danh sách liên kết (không sử dụng đệ qui):")
    dslk.InNguoc_KhongDeQui()