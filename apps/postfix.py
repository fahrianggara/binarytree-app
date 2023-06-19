from tabulate import tabulate
from apps.stack import Stack
import apps.action as action

class PostfixConverter:
    def __init__(self):
        self.stack = Stack()

    def isOperand(self, char):
          return char.isalpha() or char.isdigit()
    
    def isOperator(self, char):
        return char in ['+', '-', '*', '/', '^']
    
    def toInfix(self, expr):
        stack = self.stack

        for char in expr:
            if self.isOperand(char):
                stack.push(char)
            elif self.isOperator(char):
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.push(f"({operand2}{char}{operand1})")

        return stack.pop()
    
    def toPrefix(self, expr):
        stack = self.stack

        for char in expr:
            if self.isOperand(char):
                stack.push(char)
            elif self.isOperator(char):
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.push(f"{char}{operand2}{operand1}")

        return stack.pop()
    
    def result(self, expr):
        print(
            tabulate(
                [
                    ["Postfix (Input)", "Infix", "Prefix"],
                    [expr, self.toInfix(expr), self.toPrefix(expr)]
                ],
                tablefmt='grid'
            )
        )

    def convert():
        postfix = PostfixConverter()

        expr = input("Masukkan Notasi Postfix: ").replace(" ", "")

        if expr != "":
            action.clear()
            action.alert('Info', 'Konversi Postfix berhasil!')
            postfix.result(expr)
            action.pause()
        else:
            action.clear()
            action.alert('ERROR', 'Inputan tidak boleh kosong!')
            action.pause()

            action.clear()
            PostfixConverter.convert()