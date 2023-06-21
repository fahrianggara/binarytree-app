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
        """

        self.stack = Stack()

    def priority_level(self, char):
        """ Mengembalikan nilai prioritas dari operator 

            Params:
                self (Converter): Class Converter
                char (str): Menyimpan operator dari infix

            Returns:
                int: Nilai prioritas dari operator
        """

        if char == "(": # <- Jika buka kurung maka nilai prioritasnya 5
            return 5
        elif char == "^": # <- Jika pangkat maka nilai prioritasnya 4
            return 4
        elif char in ["/", "*", "%"]: # <- Jika perkalian, pembagian, atau modulus maka nilai prioritasnya 3
            return 3
        elif char in ["+", "-", "–"]: # <- Jika penjumlahan atau pengurangan maka nilai prioritasnya 2
            return 2
        elif char == ")": # <- Jika tutup kurung maka nilai prioritasnya 1
            return 1
        else: # <- Jika bukan operator maka nilai prioritasnya 0
            return 0
        
    def greater_than_priority(self, char, peek):
        """ Mengecek apakah char memiliki nilai prioritas yang lebih besar dari peek

            Params:
                self (Converter): Class Converter
                char (str): Menyimpan operator dari infix
                peek (str): menyimpan operator dari stack

            Returns:
                bool: True jika char memiliki nilai prioritas yang lebih besar dari peek
        """

        return self.priority_level(char) > self.priority_level(peek)
    
    def less_than_priority(self, char, peek):
        """ Mengecek apakah char memiliki nilai prioritas yang LEBIH KECIL dari peek

            Params:
                self (Converter): Class Converter
                char (str): Menyimpan operator dari infix
                peek (str): menyimpan operator dari stack

            Returns:
                bool: True jika char memiliki nilai prioritas yang LEBIH KECIL dari peek
        """

        return self.priority_level(char) < self.priority_level(peek)
    
    def less_or_equal_priority(self, char, peek):
        """ Mengecek apakah char memiliki nilai prioritas yang LEBIH KECIL ATAU SAMA DENGAN dari peek

            Params:
                self (Converter): Class Converter
                char (str): Menyimpan operator dari infix
                peek (str): menyimpan operator dari stack

            Returns:
                bool: True jika char memiliki nilai prioritas yang LEBIH KECIL ATAU SAMA DENGAN dari peek
        """

        return self.priority_level(char) <= self.priority_level(peek)
        
    def is_operand(self, char): 
        """ Mengecek apakah karakter merupakan operand (angka atau huruf)

            Params:
                self (Converter): Class Converter
                char (str): Operator yang akan dicek apakah merupakan operand

            Returns:
                bool: True jika karakter merupakan operand
        """

        return char.isalpha() or char.isdigit()
    
    # ========================================================================================================
    # Converter Infix to Postfix & Prefix
    # ========================================================================================================

    def to_postfix(self, expr, step_by_step = False, prefix_mode = False):
        """ Mengubah Infix menjadi Postfix

            Params:
                expr[expression] (str): Infix yang akan diubah menjadi Postfix
                step_by_step[optional] (bool): True jika ingin menampilkan proses konversi secara step by step

            Variables:
                stack (Stack): Stack yang digunakan untuk menyimpan operator, diambil dari class Stack
                output (list): List yang digunakan untuk menyimpan hasil konversi dari infix ke postfix
                data_table (list): List yang digunakan untuk menyimpan data yang akan ditampilkan pada tabel
                number_table (int): Menyimpan nomor urut dari setiap proses konversi
                result_stack (str): Menyimpan hasil dari stack (operator) yang akan ditampilkan pada tabel
                result_output (str): Menyimpan hasil dari output (operand) yang akan ditampilkan pada tabel
        """

        stack = self.stack
        output = []
        data_table = []
        number_table = 0
        result_stack = ""
        result_output = ""

        for char in expr: # <-- Looping setiap karakter pada expr
            number_table += 1 # <-- Menambahkan nomor urut pada setiap proses konversi

            if self.is_operand(char): # <-- Jika karakter merupakan operand (angka atau huruf)
                output.append(char) # <-- Menambahkan karakter ke dalam output

            else: # <-- Jika karakter merupakan operator
                if stack.is_empty(): # <-- Jika stack kosong
                    stack.push(char) # <-- Tambahkan operator ke stack pada posisi paling atas

                else: # <-- Jika stack tidak kosong
                    if self.greater_than_priority(char, stack.peek()):
                        """ ^Jika operator memiliki nilai prioritas yang lebih besar dari operator pada stack """

                        stack.push(char) # <-- Tambahkan operator ke stack pada posisi paling atas

                    else: 
                        if char == '(': # <-- Jika operator merupakan buka kurung
                            stack.push(char) # <-- Tambahkan operator ke stack pada posisi paling atas

                        elif char == ')': # <-- Jika operator merupakan tutup kurung

                            while stack.peek() != '(' and stack.noel() > 0: 
                                """ ^Looping selama operator pada posisi paling atas itu bukan '('
                                    dan stack tidak kosong"""
                                
                                output.append(stack.pop()) # <-- Tambahkan operator pada posisi paling atas ke dalam output
                                
                            stack.pop() # <-- Hapus operator pada posisi paling atas / akhir

                        else: # <-- Jika operator selain buka kurung dan tutup kurung

                            while stack.noel() > 0 and stack.peek() != '(' and \
                                (
                                    self.less_than_priority(char, stack.peek()) if prefix_mode 
                                    else self.less_or_equal_priority(char, stack.peek())
                                ):
                                """ ^Looping selama stack tidak kosong, operator pada posisi paling atas bukan '(',
                                    dan apa bila prefix_mode = True, maka operator memiliki nilai prioritas yang LEBIH KECIL 
                                    dari operator pada posisi paling atas,dan jika prefix_mode = False maka operator memiliki
                                    nilai prioritas yang LEBIH KECIL ATAU SAMA DENGAN operator pada posisi paling atas"""
                                
                                output.append(stack.pop()) # <-- Tambahkan operator pada posisi paling atas ke dalam output

                            stack.push(char) # <-- Tambahkan operator ke stack pada posisi paling atas

            result_output = " ".join(output) # <-- Mengubah list output menjadi string
            result_stack = " ".join(stack.items) # <-- Mengubah list stack menjadi string
            data_table.append([number_table, expr, char, result_output, result_stack]) # <-- Menambahkan data ke dalam list data_table

        while not stack.is_empty(): # <-- Looping selama stack tidak kosong
            output.append(stack.pop()) # <-- Tambahkan operator pada posisi paling atas ke dalam output

        result_output = " ".join(output) 
        result_stack = " ".join(stack.items)
        data_table.append([number_table + 1, expr, '', result_output, result_stack])

        if prefix_mode: # <-- Jika prefix_mode = True
            
            # Menambahkan data lagi ke dalam list data_table untuk menampilkan prefix dibalik
            data_table.append([number_table + 2, expr, '', result_output[::-1], result_stack]) 

        # Jika step_by_step = True, maka return data_table, jika tidak maka return result_output
        return data_table if step_by_step else result_output

    def to_prefix(self, expr, step_by_step = False, reverse = False):
        """ Mengubah Infix menjadi Prefix secara step by step

            Parameters:
                expr (str): Karakter infix yang akan diubah menjadi prefix
                step_by_step (bool): True jika ingin menampilkan proses konversi secara step by step
                reverse (bool): True jika ingin menampilkan hasil konversi secara terbalik (dibalik)

            Vars:
                reverse_expr (str): Menyimpan hasil reverse (dibalik) dari expr

            Returns:
                list: Hasil konversi dari Infix ke Prefix secara step by step
        """
         
        reverse_expr = ""

        for char in reversed(expr): # <-- Looping setiap karakter pada expr secara terbalik

            if char == "(": # <-- Jika karakter merupakan buka kurung
                reverse_expr += ")" # <-- Ditukar dengan tutup kurung
            elif char == ")": # <-- Jika karakter merupakan tutup kurung
                reverse_expr += "(" # <-- Ditukar dengan buka kurung
            else: # <-- Jika karakter bukan buka kurung dan tutup kurung
                reverse_expr += char # <-- Tambahkan karakter ke dalam reverse_expr

    
        prefix = self.to_postfix(reverse_expr, step_by_step, True) # <-- Mengubah reverse_expr menjadi postfix
        
        #Jika step_by_step = True, maka return prefix, jika tidak maka return prefix yang dibalik
        return prefix if step_by_step else prefix[::-1]
    
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
                    [expr, self.to_postfix(expr), self.to_prefix(expr, False, True)] # <-- Data table
                ],
                tablefmt='grid' # <-- Style table
            )
        )

        print(f"\nStep by Step Infix => Postfix:")
        print( # <-- Menampilkan hasil konversi dari Infix ke Postfix secara step by Step
            tabulate(
                self.to_postfix(expr, True), # <-- Memanggil method step_by_step_postfix (Data table)
                headers=['Step', 'Input', 'Char', 'Output', 'Stack'],
                tablefmt='grid',
            )
        )

        print(f"\nStep by Step Infix => Prefix:")
        print( # <-- Menampilkan hasil konversi dari Infix ke Prefix secara step by Step
            tabulate(
                self.to_prefix(expr, True),
                headers=['Step', 'Input', 'Char', 'Output', 'Stack'],
                tablefmt='grid', 
            )
        )