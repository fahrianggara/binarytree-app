from tabulate import tabulate
from apps.stack import Stack
import apps.action as action

class PrefixConverter:
    def __init__(self):
        self.stack = Stack()

    def isOperand(self, char):
        return char.isalpha() or char.isdigit()

    def isOperator(self, char):
        return char in ['+', '-', '*', '/', '^']

    def toInfix(self, expr):
        stack = self.stack

        for char in reversed(expr):
            if self.isOperand(char):
                stack.push(char)
            elif self.isOperator(char):
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.push(f"({operand1}{char}{operand2})")
        
        return stack.pop()

    def toPostfix(self, expr):
        stack = self.stack

        for char in reversed(expr):
            if self.isOperand(char):
                stack.push(char)
            elif self.isOperator(char):
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.push(f"{operand1}{operand2}{char}")
        
        return stack.pop()

    def result(self, expr):
        print(
            tabulate(
                [
                    ["Prefix (Input)", "Infix", "Postfix"],
                    [expr, self.toInfix(expr), self.toPostfix(expr)]
                ],
                tablefmt='grid'
            )
        )

    def convert():
        prefix = PrefixConverter()

        expr = input("Masukkan Notasi Prefix: ").replace(" ", "")

        if expr != "":
            action.clear()
            action.alert('Info', 'Konversi Prefix berhasil!')
            prefix.result(expr)
            action.pause()
        else:
            action.clear()
            action.alert('ERROR', 'Inputan tidak boleh kosong!')
            action.pause()

            action.clear()
            PrefixConverter.convert()
