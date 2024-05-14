class HanoiTower:
    def __init__(self, n):
        self.n = n
        self.tower1 = list(range(n, 0, -1))
        self.tower2 = []
        self.tower3 = []

    def move(self, n, from_tower, to_tower, aux_tower):
        if n == 1:
            disk = from_tower.pop()
            to_tower.append(disk)
            print(f"Di chuyển đĩa {disk} từ tháp {from_tower} đến tháp {to_tower}")
        else:
            self.move(n-1, from_tower, aux_tower, to_tower)
            self.move(1, from_tower, to_tower, aux_tower)
            self.move(n-1, aux_tower, to_tower, from_tower)

    def move_towers(self):
        self.move(self.n, self.tower1, self.tower3, self.tower2)

if __name__ == "__main__":
    n = 3
    hanoi = HanoiTower(n)
    hanoi.move_towers()