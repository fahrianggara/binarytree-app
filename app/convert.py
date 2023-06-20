from tabulate import tabulate # <-- Library untuk membuat tabel
from app import * # <-- Import semua yang ada di folder app

# ========================================================================================================
# Section Stack: Membuat Operasi Stack. LIFO (Last In First Out) 
# ========================================================================================================

class Stack:

    def __init__(self): # <-- Inisialisasi properties dari class Stack
        self.items = []

    def is_empty(self): # <-- Mengecek apakah list kosong
        return self.items == []
    
    def push(self, item): # <-- Menambahkan item pada posisi paling atas / akhir
        self.items.append(item)

    def pop(self): # <-- Menghapus item pada posisi paling atas / akhir
        return self.items.pop()
    
    def peek(self): # <-- Mendapatkan item pada posisi paling atas / akhir
        return self.items[self.noel() - 1]
    
    def noel(self): # <-- Menghitung jumlah item pada list
        return len(self.items)
    
# ========================================================================================================
# Section Converter: Infix => Postfix & Prefix
# ========================================================================================================
    
class Converter:

    # ========================================================================================================
    # Properties & Initializer
    # ========================================================================================================

    def __init__(self):
        """ Inisialisasi properties dari class Converter
        
            Var:
                stack (Stack): Stack yang digunakan untuk menyimpan operator, diambil dari class Stack
                precedence (dict): Dictionary yang berisi operator dan nilai prioritasnya
        """

        self.stack = Stack()
        self.precedence = {'+':2, '-':2, '*':3, '/':3, '%':3, '^':4}

    def precedence_level(self, char):
        """ Mengembalikan nilai prioritas dari operator 

            Parameters:
                char (str): Menyimpan operator dari infix

            Returns:
                int: Nilai prioritas dari operator
        """

        if char == "(": # Jika buka kurung maka nilai prioritasnya 5
            return 5
        elif char == "^": # Jika pangkat maka nilai prioritasnya 4
            return 4
        elif char in ["*", "/", "%"]: # Jika perkalian, pembagian, atau modulus maka nilai prioritasnya 3
            return 3
        elif char in ["+", "-", "–"]: # Jika penjumlahan atau pengurangan maka nilai prioritasnya 2
            return 2
        elif char == ")": # Jika tutup kurung maka nilai prioritasnya 1
            return 1
        else: # Jika bukan operator maka nilai prioritasnya 0
            return 0
    
    def less_or_equal_priority(self, char, peek):
        """ Mengecek apakah operator char memiliki nilai prioritas yang lebih kecil atau sama dengan operator peek

            Parameters:
                char (str): Menyimpan operator dari infix
                peek (str): menyimpan operator dari stack

            Returns:
                bool: True jika char memiliki nilai prioritas yang lebih kecil atau sama dengan peek
        """

        if char not in self.precedence:
            return False
        
        if peek not in self.precedence:
            return False
        
        return self.precedence[char] <= self.precedence[peek]
    
    def is_operand(self, char): 
        """ Mengecek apakah karakter merupakan operand (angka atau huruf)

            Parameters:
                char (str): Operator yang akan dicek apakah merupakan operand

            Returns:
                bool: True jika karakter merupakan operand
        """

        return char.isalpha() or char.isdigit()
    
    # ========================================================================================================
    # Converter Infix to Postfix & Prefix
    # ========================================================================================================

    def to_postfix(self, expr):
        """ Mengubah Infix menjadi Postfix

            Parameters:
                expr[expression] (str): Infix yang akan diubah menjadi Postfix

            Vars:
                self_stack (Stack): Stack yang digunakan untuk menyimpan operator, diambil dari class Stack
                result_output (str): Menyimpan hasil konversi dari Infix ke Postfix

            Returns:
                str: Hasil konversi dari Infix ke Postfix
        """

        self_stack = self.stack
        result_output = ''

        for char in expr: # <-- Looping setiap karakter pada expr

            if self.is_operand(char): # <-- Jika karakter merupakan operand (angka atau huruf)
                result_output += char # <-- Tambahkan karakter ke result_output

            else: # <-- Jika karakter merupakan operator
                if char == '(': # <-- Jika karakter adalah '(' buka kurung
                    self_stack.push(char) # <-- Tambahkan operator ke stack pada posisi paling atas / akhir

                elif char == ')': # <-- Jika karakter adalah ')' tutup kurung
                    operator = self_stack.pop() # <-- Ambil operator pada posisi paling atas / akhir

                    while operator != '(': # <-- Looping selama operator bukan '(' buka kurung
                        result_output += operator # <-- Tambahkan operator ke result_output
                        operator = self_stack.pop() # <-- Ambil operator pada posisi paling atas / akhir

                else: # <-- Jika karakter adalah operator selain '(' buka kurung dan ')' tutup kurung

                    while not self_stack.is_empty() \
                        and self.less_or_equal_priority(char, self_stack.peek()):
                        """ Looping selama stack tidak kosong dan operator pada posisi paling atas / akhir 
                            yang memiliki nilai prioritas yang lebih besar dari operator char 
                        """

                        result_output += self_stack.pop() # <-- Tambahkan operator ke result_output

                    self_stack.push(char) # <-- Tambahkan operator ke stack pada posisi paling atas / akhir

        while not self_stack.is_empty(): # <-- Looping selama stack tidak kosong
            result_output += self_stack.pop() # <-- Tambahkan operator ke result_output

        return result_output # <-- Kembalikan hasil konversi dari Infix ke Postfix

    def to_prefix(self, expr):
        """ Mengubah Infix menjadi Prefix

            Paramaters:
                expr (str): Karakter infix yang akan diubah menjadi prefix

            Vars:
                rvs_expr (str): Menyimpan hasil reverse (dibalik) dari expr

            Returns:
                str: Hasil konversi dari Infix ke Prefix
        """

        rvs_expr = ""

        for char in reversed(expr): # <-- Looping setiap karakter pada expr secara terbalik
            if char == '(':
                rvs_expr += ')'
            elif char == ')':
                rvs_expr += '('
            else: # <-- Jika karakter adalah operator selain '(' buka kurung dan ')' tutup kurung
                rvs_expr += char

        prefix = self.to_postfix(rvs_expr) # <-- Mengubah rvs_expr menjadi postfix
        return prefix[::-1] # <-- Mengembalikan hasil reverse dari prefix
    
    # ========================================================================================================
    # Step by Step Converter Infix to Postfix & Prefix
    # ========================================================================================================

    def step_by_step_postfix(self, expr):
        """ Mengubah Infix menjadi Postfix secara step by step

            Parameters:
                expr (str): Karakter infix yang akan diubah menjadi postfix

            Vars:
                self_stack (Stack): Stack yang digunakan untuk menyimpan operator, diambil dari class Stack
                result_output (str): Menyimpan hasil konversi dari Infix ke Postfix
                result_stack (str): Menyimpan operator yang ada pada stack
                output (list): Menyimpan hasil konversi dari Infix ke Postfix secara step by step
                table (list): Menyimpan hasil konversi dari Infix ke Postfix secara step by step

            Returns:
                list: Hasil konversi dari Infix ke Postfix secara step by step
        """

        self_stack = self.stack
        result_output = ''
        result_stack = ''
        number = 0
        table = []
        output = []

        for char in expr: # <-- Looping setiap karakter pada expr
            number += 1 # <-- Menambahkan nilai number dengan 1 untuk urutan step

            if self.is_operand(char): # <-- Jika karakter merupakan operand (angka atau huruf)
                output.append(char) # <-- Tambahkan karakter ke output
            else:
                if self_stack.noel() == 0: # <-- Jika stack kosong
                    self_stack.push(char) # <-- Tambahkan operator ke stack pada posisi paling atas / akhir

                else: # <-- Jika stack tidak kosong
                    if self.precedence_level(char) > self.precedence_level(self_stack.peek()):
                        """ Jika operator char memiliki nilai prioritas yang lebih besar dari 
                        operator pada posisi paling atas / akhir"""
                    
                        self_stack.push(char) # <-- Tambahkan operator ke stack pada posisi paling atas / akhir

                    elif self.precedence_level(char) <= self.precedence_level(self_stack.peek()):
                        """ Jika operator char memiliki nilai prioritas yang lebih kecil atau sama dengan dari
                        operator pada posisi paling atas / akhir"""
                    
                        if char == ")": # <-- Jika karakter adalah ')' tutup kurung

                            while self_stack.peek() != "(" and self_stack.noel() > 0:
                                """ Looping selama operator pada posisi paling atas / akhir bukan '(' buka kurung 
                                    dan stack tidak kosong"""
                                
                                output.append(self_stack.pop()) # <-- Tambahkan operator ke output

                            self_stack.pop() # <-- Hapus operator pada posisi paling atas / akhir

                        else: # <-- Jika karakter adalah operator selain ')' tutup kurung

                            while self_stack.noel() > 0 and self_stack.peek() != "(":
                                """ Looping selama operator pada posisi paling atas / akhir bukan '(' buka kurung 
                                    dan stack tidak kosong"""
                                
                                output.append(self_stack.pop()) # <-- Tambahkan operator ke output

                            self_stack.push(char) # <-- Tambahkan operator ke stack pada posisi paling atas / akhir


            result_output = ''.join(output) # <-- Mengubah list output menjadi string
            result_stack = ''.join(self_stack.items) # <-- Mengubah list items pada stack menjadi string
            table.append([number, expr, char, result_output, result_stack]) # <-- Tambahkan data ke table

        while not self_stack.is_empty() : # <-- Looping selama stack tidak kosong
            output.append(self_stack.pop()) # <-- Tambahkan operator ke output

        return table # <-- Kembalikan hasil konversi dari Infix ke Postfix secara step by step
    
    def step_by_step_prefix(self, expr):
        """ Mengubah Infix menjadi Prefix secara step by step

            Parameters:
                expr (str): Karakter infix yang akan diubah menjadi prefix

            Vars:
                rvs_expr (str): Menyimpan hasil reverse (dibalik) dari expr

            Returns:
                list: Hasil konversi dari Infix ke Prefix secara step by step
        """

        rvs_expr = ""

        for char in reversed(expr): # <-- Looping setiap karakter pada expr secara terbalik
            if char == '(':
                rvs_expr += ')'
            elif char == ')':
                rvs_expr += '('
            else: # <-- Jika karakter adalah operator selain '(' buka kurung dan ')' tutup kurung
                rvs_expr += char

        prefix = self.step_by_step_postfix(rvs_expr) # <-- Mengubah rvs_expr menjadi postfix
        return prefix # <-- Mengembalikan hasil reverse dari prefix
    
    # ========================================================================================================
    # Converter Result
    # ========================================================================================================

    def convert(self, expr):
        """ Menampilkan hasil konversi dari Infix ke Postfix & Prefix
        
            Parameters:
                expr (str): Karakter infix yang akan diubah menjadi postfix & prefix
        """

        print(f"\nHasil Konversi Infix => Postfix & Prefix:")
        print( # <-- Menampilkan hasil konversi dari Infix ke Postfix & Prefix
            tabulate(
                [
                    ["Infix", "Postfix", "Prefix"], # <-- Header table
                    [expr, self.to_postfix(expr), self.to_prefix(expr)] # <-- Data table
                ],
                tablefmt='grid' # <-- Style table
            )
        )
 
        print(f"\nStep by Step Infix => Postfix:")
        print( # <-- Menampilkan hasil konversi dari Infix ke Postfix secara step by Step
            tabulate(
                self.step_by_step_postfix(expr), # <-- Memanggil method step_by_step_postfix (Data table)
                headers=['#', 'Input', 'Symbol', 'Output', 'Stack'],
                tablefmt='grid',
            )
        )

        print(f"\nStep by Step Infix => Prefix:")
        print( # <-- Menampilkan hasil konversi dari Infix ke Prefix secara step by Step
            tabulate(
                self.step_by_step_prefix(expr),
                headers=['#', 'Input', 'Symbol', 'Output', 'Stack'],
                tablefmt='grid', 
            )
        )