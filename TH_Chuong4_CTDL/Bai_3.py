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