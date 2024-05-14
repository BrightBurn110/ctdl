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
    def DaoNguoc(self):
        stack = []
        current = self.Head
        while current:
            stack.append(current)
            current = current.Next
        self.Head = stack.pop()
        temp = self.Head
        while stack:
            temp.Next = stack.pop()
            temp = temp.Next
        temp.Next = None
    def InDanhSach(self):
        current = self.Head
        while current:
            print(current.Info, end=" ")
            current = current.Next
        print()

if __name__ == "__main__":
    dslk = DSLK()
    dslk.Them(1)
    dslk.Them(2)
    dslk.Them(3)
    dslk.Them(4)

    print("\nDanh sách liên kết trước khi đảo ngược:")
    dslk.InDanhSach()

    dslk.DaoNguoc()

    print("Danh sách liên kết sau khi đảo ngược:")
    dslk.InDanhSach()