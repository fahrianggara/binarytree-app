from tabulate import tabulate 
from app import * 

# ========================================================================================================
# Section Stack: Membuat Operasi Stack. LIFO (Last In First Out) 
# ========================================================================================================

class Stack:

    def __init__(self): 
        self.items = []

    def is_empty(self): 
        return self.items == []
    
    def push(self, item): 
        self.items.append(item)

    def pop(self): 
        return self.items.pop()
    
    def peek(self): 
        return self.items[self.noel() - 1]
    
    def noel(self): 
        return len(self.items)
    
# ========================================================================================================
# Section Converter: Infix => Postfix & Prefix
# ========================================================================================================
    
class Converter:

    # ========================================================================================================
    # Properties & Initializer
    # ========================================================================================================

    def __init__(self):
        self.stack = Stack()

    def priority_level(self, char):
        if char == "(":
            return 5
        elif char == "^":
            return 4
        elif char in ["/", "*", "%"]:
            return 3
        elif char in ["+", "-", "–"]:
            return 2
        elif char == ")":
            return 1
        else:
            return 0
        
    def greater_than_priority(self, char, peek):
        return self.priority_level(char) > self.priority_level(peek)
    
    def less_than_priority(self, char, peek):
        return self.priority_level(char) < self.priority_level(peek)
    
    def less_or_equal_priority(self, char, peek):
        return self.priority_level(char) <= self.priority_level(peek)
        
    def is_operand(self, char):
        return char.isalpha() or char.isdigit()
    
    # ========================================================================================================
    # Converter Infix to Postfix & Prefix
    # ========================================================================================================

    def to_postfix(self, expr, step_by_step = False, prefix_mode = False):
        stack = self.stack
        output = []
        data_table = []
        number_table = 0
        result_stack = ""
        result_output = ""

        for char in expr: 
            number_table += 1

            if self.is_operand(char): 
                output.append(char) 

            else: 
                if stack.is_empty(): 
                    stack.push(char) 

                else: 
                    if self.greater_than_priority(char, stack.peek()):
                        stack.push(char) 

                    else: 
                        if char == '(': 
                            stack.push(char) 

                        elif char == ')': 
                            while stack.peek() != '(' and stack.noel() > 0:
                                output.append(stack.pop()) 
                                
                            stack.pop() 

                        else: 
                            while stack.noel() > 0 and stack.peek() != '(' and \
                                (
                                    self.less_than_priority(char, stack.peek()) 
                                    if prefix_mode 
                                    else self.less_or_equal_priority(char, stack.peek())
                                ):
                                output.append(stack.pop()) 

                            stack.push(char) 

            result_output = " ".join(output) 
            result_stack = " ".join(stack.items) 
            data_table.append([number_table, expr, char, result_output, result_stack])

        while not stack.is_empty(): 
            output.append(stack.pop()) 

        result_output = " ".join(output) 
        result_stack = " ".join(stack.items)
        data_table.append([number_table + 1, expr, '', result_output, result_stack])

        if prefix_mode:
            data_table.append([number_table + 2, expr, '', result_output[::-1], result_stack])

        return data_table if step_by_step else result_output

    def to_prefix(self, expr, step_by_step = False, reverse = False):
        reverse_expr = ""

        for char in reversed(expr): 

            if char == "(": 
                reverse_expr += ")" 
            elif char == ")": 
                reverse_expr += "(" 
            else: 
                reverse_expr += char 

        prefix = self.to_postfix(reverse_expr, step_by_step, True) 
        return prefix if step_by_step else prefix[::-1]
    
    # ========================================================================================================
    # Converter Result
    # ========================================================================================================

    def convert(self, expr):
        print(f"\nHasil Konversi Infix => Postfix & Prefix:")
        print( 
            tabulate(
                [
                    ["Infix", "Postfix", "Prefix"], 
                    [expr, self.to_postfix(expr), self.to_prefix(expr, False, True)] 
                ],
                tablefmt='grid' 
            )
        )

        print(f"\nStep by Step Infix => Postfix:")
        print( 
            tabulate(
                self.to_postfix(expr, True), 
                headers=['Step', 'Input', 'Char', 'Output', 'Stack'],
                tablefmt='grid',
            )
        )

        print(f"\nStep by Step Infix => Prefix:")
        print( 
            tabulate(
                self.to_prefix(expr, True),
                headers=['Step', 'Input', 'Char', 'Output', 'Stack'],
                tablefmt='grid', 
            )
        )