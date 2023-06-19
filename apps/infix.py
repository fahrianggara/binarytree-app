from tabulate import tabulate
from apps.stack import Stack
import apps.action as action

class InfixConverter:
    def __init__(self):
        self.stack = Stack()
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    
    def lessOrEqualPriority(self, a, b):
        if a not in self.precedence:
            return False
        
        if b not in self.precedence:
            return False
        
        return self.precedence[a] <= self.precedence[b]
    
    def isOperand(self, char):
        return char.isalpha() or char.isdigit()
    
    def isBukaKurung(self, char):
        return char == '('
    
    def isTutupKurung(self, char):
        return char == ')'
    
    # =================================================================================================
    # CONVERTER
    # =================================================================================================
    
    def toPostfix(self, expr):
        stack = self.stack
        output = ''

        for char in expr:
            if self.isOperand(char):
                output += char
            else:
                if self.isBukaKurung(char):
                    stack.push(char)
                elif self.isTutupKurung(char):
                    operator = stack.pop()

                    while not self.isBukaKurung(operator):
                        output += operator
                        operator = stack.pop()
                else:
                    while (not stack.isEmpty()) and self.lessOrEqualPriority(char, stack.peek()):
                        output += stack.pop()

                    stack.push(char)

        while (not stack.isEmpty()):
            output += stack.pop()

        return output
    
    def toPrefix(self, expr):
        reverse_expr = ''

        for char in expr[::-1]:
            if char == '(':
                reverse_expr += ')'
            elif char == ')':
                reverse_expr += '('
            else:
                reverse_expr += char
        
        reverse_postfix = self.toPostfix(reverse_expr)
        return reverse_postfix[::-1]
    
    # =================================================================================================
    # STEP BY STEP
    # =================================================================================================
    
    def stepByStepPostfix(self, expr):
        stack = self.stack
        output = ''
        operator = ''
        table = []

        for char in expr:
            if self.isOperand(char):
                output += char
            else:
                operator += char

                if self.isBukaKurung(char):
                    stack.push(char)
                elif self.isTutupKurung(char):
                    operator = stack.pop()

                    while not self.isBukaKurung(operator):
                        output += operator
                        operator = stack.pop()
                else:
                    while (not stack.isEmpty()) and self.lessOrEqualPriority(char, stack.peek()):
                        output += stack.pop()

                    stack.push(char)

            table.append([expr, output, operator])

        while (not stack.isEmpty()):
            output += stack.pop()

        return table
    
    def stepByStepPrefix(self, expr):
        reverse_expr = ''

        for char in expr[::-1]:
            if char == '(':
                reverse_expr += ')'
            elif char == ')':
                reverse_expr += '('
            else:
                reverse_expr += char
        
        return self.stepByStepPostfix(reverse_expr)
    
    # =================================================================================================
    # RESULT
    # =================================================================================================

    def result(self, expr):
        print(f"\nHasil Konversi Infix => Prefix & Postfix:")

        print(
            tabulate(
                [
                    ["Infix (Input)", "Prefix", "Postfix"],
                    [expr, self.toPrefix(expr), self.toPostfix(expr)]
                ],
                tablefmt='grid'
            )
        )

        print(f"\nStep by step Infix => Postfix:")
        print(
            tabulate(
                self.stepByStepPostfix(expr),
                headers=['Input', 'Output Stack', 'Operator Stack'],
                tablefmt='grid'
            )
        )

        print(f"\nStep by step Infix => Prefix:")
        print(
            tabulate(
                self.stepByStepPrefix(expr),
                headers=['Input', 'Output Stack', 'Operator Stack'],
                tablefmt='grid'
            )
        )

    def convert():
        infix = InfixConverter()

        expr = input("Masukkan Notasi Infix: ").replace(" ", "")

        if expr != "":
            action.clear()
            infix.result(expr)
            action.pause()
        else:
            action.clear()
            action.alert('ERROR', 'Inputan tidak boleh kosong!')
            action.pause()

            action.clear()
            InfixConverter.convert()