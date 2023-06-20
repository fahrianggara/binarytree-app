from app import * # <-- Import semua fungsi yang ada di folder app

if __name__ == "__main__": # <-- Main program

    while True: # <-- Looping program sampai user memilih untuk keluar
        clear_screen() # <-- Membersihkan layar terminal

        infix = Converter() # <-- Membuat objek dari class Converter
        expr = input("Masukkan Notasi Infix (q untuk exit): ").replace(" ", "") # <-- Inputan user

        if expr != "": # <-- Jika inputan user tidak kosong
            if expr.lower() == "q": # <-- Jika inputan user adalah q (keluar dari program)
                clear_screen()
                exit_program()
                
            else: # <-- Jika inputan user bukan q (konversi infix ke postfix dan prefix)
                clear_screen()
                infix.convert(expr)
                pause_program()

        else: # <-- Jika inputan user kosong
            clear_screen()
            alert('ERROR', 'Inputan tidak boleh kosong!')
            pause_program()
