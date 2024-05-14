class Node:
    def __init__(self, heSo, soMu):
        self.HeSo = heSo
        self.SoMu = soMu
        self.KeTiep = None
class DaThuc:
    def __init__(self):
        self.Head = None
    def Them(self, heSo, soMu):
        new_node = Node(heSo, soMu)
        if self.Head is None:
            self.Head = new_node
            return
        if soMu > self.Head.SoMu:
            new_node.KeTiep = self.Head
            self.Head = new_node
            return
        current = self.Head
        while current.KeTiep is not None and current.KeTiep.SoMu > soMu:
            current = current.KeTiep
        new_node.KeTiep = current.KeTiep
        current.KeTiep = new_node
    def InDaThuc(self):
        current = self.Head
        while current is not None:
            print(current.HeSo, 'x^', current.SoMu, end = " ")
            if current.KeTiep is not None:
                print("+", end = " ")
            current = current.KeTiep
        print()

if __name__ == "__main__":
    dathuc = DaThuc()
    dathuc.Them(3, 2)
    dathuc.Them(5, 1)
    dathuc.Them(2, 4)

    print("Da thuc sau khi them:")
    dathuc.InDaThuc()