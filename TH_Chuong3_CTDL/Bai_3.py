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

    def Cong(self, dathuc2):
        result = DaThuc()
        current1 = self.Head
        current2 = dathuc2.Head

        while current1 or current2:
            if current1 and current2:
                if current1.SoMu > current2.SoMu:
                    result.Them(current1.HeSo, current1.SoMu)
                    current1 = current1.KeTiep
                elif current1.SoMu < current2.SoMu:
                    result.Them(current2.HeSo, current2.SoMu)
                    current2 = current2.KeTiep
                else:
                    result.Them(current1.HeSo + current2.HeSo, current1.SoMu)
                    current1 = current1.KeTiep
                    current2 = current2.KeTiep
            elif current1:
                result.Them(current1.HeSo, current1.SoMu)
                current1 = current1.KeTiep
            else:
                result.Them(current2.HeSo, current2.SoMu)
                current2 = current2.KeTiep

        result.RutGon()
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
    dathuc1 = DaThuc()
    dathuc1.Them(3, 2)
    dathuc1.Them(-5, 1)
    dathuc1.Them(2, 4)

    dathuc2 = DaThuc()
    dathuc2.Them(4, 3)
    dathuc2.Them(1, 2)
    dathuc2.Them(2, 1)

    print("Da thuc 1:")
    dathuc1.InDaThuc()
    print("Da thuc 2:")
    dathuc2.InDaThuc()

    dathuc3 = dathuc1.Cong(dathuc2)
    print("\nDa thuc sau khi cong:")
    dathuc3.InDaThuc()