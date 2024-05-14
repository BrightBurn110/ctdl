### Bai 1
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

### Bai 2
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

### Bai 3
class BieuThuc:
    def __init__(self, expression):
        self.expression = expression

    @staticmethod
    def la_toan_tu(char):
        return char in ['+', '-', '*', '/']

    @staticmethod
    def la_so(operand):
        try:
            float(operand)
            return True
        except ValueError:
            return False

    def GiaTri(self):
        elements = self.expression.split()
        operand_stack = []
        operator_stack = []
        for element in elements:
            if self.la_so(element):
                operand_stack.append(float(element))
            elif self.la_toan_tu(element):
                while (operator_stack and
                       operator_stack[-1] != '(' and
                       (element == '+' or element == '-') and
                       (operator_stack[-1] == '*' or operator_stack[-1] == '/')):
                    operator = operator_stack.pop()
                    operand2 = operand_stack.pop()
                    operand1 = operand_stack.pop()
                    if operator == '+':
                        operand_stack.append(operand1 + operand2)
                    elif operator == '-':
                        operand_stack.append(operand1 - operand2)
                    elif operator == '*':
                        operand_stack.append(operand1 * operand2)
                    elif operator == '/':
                        operand_stack.append(operand1 / operand2)
                operator_stack.append(element)
            elif element == '(':
                operator_stack.append(element)
            elif element == ')':
                while operator_stack[-1] != '(':
                    operator = operator_stack.pop()
                    operand2 = operand_stack.pop()
                    operand1 = operand_stack.pop()
                    if operator == '+':
                        operand_stack.append(operand1 + operand2)
                    elif operator == '-':
                        operand_stack.append(operand1 - operand2)
                    elif operator == '*':
                        operand_stack.append(operand1 * operand2)
                    elif operator == '/':
                        operand_stack.append(operand1 / operand2)
                operator_stack.pop()

        while operator_stack:
            operator = operator_stack.pop()
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            if operator == '+':
                operand_stack.append(operand1 + operand2)
            elif operator == '-':
                operand_stack.append(operand1 - operand2)
            elif operator == '*':
                operand_stack.append(operand1 * operand2)
            elif operator == '/':
                operand_stack.append(operand1 / operand2)
        return operand_stack.pop()

if __name__ == "__main__":
    expression = "3 + ( 4 * 2 ) / 6 - 5"
    bt = BieuThuc(expression)
    print("Giá trị của biểu thức:", bt.GiaTri())

### Bai 4
class BieuThuc:
    def __init__(self, expression):
        self.expression = expression

    @staticmethod
    def la_toan_tu(char):
        return char in ['+', '-', '*', '/']

    @staticmethod
    def la_so(operand):
        try:
            float(operand)
            return True
        except ValueError:
            return False

    def HauTo(self):
        elements = self.expression.split()
        output = []
        operator_stack = []

        for element in elements:
            if self.la_so(element):
                output.append(element)
            elif element == '(':
                operator_stack.append(element)
            elif element == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()
            elif self.la_toan_tu(element):
                while (operator_stack and
                       operator_stack[-1] != '(' and
                       ((element == '+' or element == '-') and
                        (operator_stack[-1] == '*' or operator_stack[-1] == '/'))):
                    output.append(operator_stack.pop())
                operator_stack.append(element)

        while operator_stack:
            output.append(operator_stack.pop())

        return ' '.join(output)

if __name__ == "__main__":
    expression = "2 + 3 * 5"
    bt = BieuThuc(expression)
    print("Biểu thức hậu tố:", bt.HauTo())

### Bai 5
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
