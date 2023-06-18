from tabulate import tabulate
from apps.stack import Stack
import apps.action as action

class Convert: # Infix to Prefix and Postfix
    def __init__(self):
        self.stack = Stack()
        self.priority = {'+':1, '-':1, '*':2, '/':2, '^':3}
    
    def lessOrEqualPriority(self, a, b):
        if a not in self.priority:
            return False
        
        if b not in self.priority:
            return False
        
        return self.priority[a] <= self.priority[b]
    
    def isOperator(self, x):
        return x in ['+', '-', '*', '/', '^']
    
    def isOperand(self, char):
        return char.isalpha() or char.isdigit()
    
    def isBukaKurung(self, char):
        return char == '('
    
    def isTutupKurung(self, char):
        return char == ')'
    
    def infixToPostfix(self, expr): # expr = expression
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
    
    def infixToPrefix(self, expr):
        reverse_expr = ''

        for char in expr[::-1]:
            if char == '(':
                reverse_expr += ')'
            elif char == ')':
                reverse_expr += '('
            else:
                reverse_expr += char
        
        reverse_postfix = self.infixToPostfix(reverse_expr)
        return reverse_postfix[::-1]
    
    def infixConvert(self, expr):
        try:
            result = eval(expr)
        except:
            result = expr

        print(
            tabulate(
                [
                    ["Infix", "Prefix", "Postfix",  "Hasil"],
                    [expr, self.infixToPrefix(expr), self.infixToPostfix(expr),  result]
                ],
                tablefmt='grid'
            )
        )

    def start():
        convert = Convert()

        while True:
            action.clear()
            expr = input("Silahkan masukkan notasi infix (q untuk keluar): ").replace(" ", "")

            if expr != "":
                if expr.lower() == 'q':
                    action.clear()
                    action.exitProgram()
                else:
                    action.clear()
                    convert.infixConvert(expr)
                    action.pause()
            else:
                action.clear()
                action.alert("Warning", "Inputan tidak boleh kosong!")
                action.pause()