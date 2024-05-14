class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

class DaThuc:
    def __init__(self):
        self.Head = None

    def Them(self, heso, somu):
        new_node = Node(heso, somu)

        if self.Head is None:
            self.Head = new_node
            return

        if somu > self.Head.SoMu:
            new_node.KeTiep = self.Head
            self.Head = new_node
            return

        current = self.Head

        while current.KeTiep is not None and current.KeTiep.SoMu > somu:
            current = current.KeTiep

        new_node.KeTiep = current.KeTiep
        current.KeTiep = new_node

    def RutGon(self):
        if self.Head is None:
            return

        current = self.Head
        prev = None

        while current and current.KeTiep:
            if current.SoMu == current.KeTiep.SoMu:
                current.HeSo += current.KeTiep.HeSo
                current.KeTiep = current.KeTiep.KeTiep
            if current.HeSo == 0:
                if prev:
                    prev.KeTiep = current.KeTiep
                else:
                    self.Head = current.KeTiep
            else:
                prev = current
            current = current.KeTiep

    def Chep(self):
        result = DaThuc()
        current = self.Head

        while current:
            result.Them(current.HeSo, current.SoMu)
            current = current.KeTiep

        return result

    def InDaThuc(self):
        current = self.Head
        while current is not None:
            print(current.HeSo, "x^", current.SoMu, end=" ")
            if current.KeTiep is not None:
                print("+", end=" ")
            current = current.KeTiep
        print()

if __name__ == "__main__":
    dathuc = DaThuc()
    dathuc.Them(3, 2)
    dathuc.Them(-5, 1)
    dathuc.Them(2, 4)

    print("Da thuc truoc khi sao chep:")
    dathuc.InDaThuc()

    dathuc_copy = dathuc.Chep()
    print("\nDa thuc sau khi sao chep:")
    dathuc_copy.InDaThuc()