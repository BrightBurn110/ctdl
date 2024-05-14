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