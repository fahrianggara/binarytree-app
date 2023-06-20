import os

def clear_screen():
    """ Fungsi ini untuk membersihkan layar terminal """

    # Jika os.name adalah nt (Windows), jika bukan maka akan dijalankan perintah clear (Linux)
    os.system('cls' if os.name == 'nt' else 'clear')

def alert(title, message):
    """ Fungsi ini untuk menampilkan pesan alert

        Args:
            title (str): Menyimpan judul dari pesan
            message (str): Menyimpan isi dari pesan
    """

    # Jika title adalah None (tidak ada judul), jika ada judul maka akan ditampilkan
    print('-' * 40) if title is None else print(f"-- {title} {32 * '-'}") 
    print(f"{message}")
    print('-' * 40)

def pause_program():
    """ Fungsi ini untuk memberhentikan program sementara """

    input('\n>> Tekan ENTER untuk melanjutkan <<')

def exit_program():
    """ Fungsi ini untuk keluar dari program """

    pilihan = input("Apakah kamu yakin akan keluar dari program? [Y/T]: ").upper()

    if pilihan == 'Y': # <-- Jika user memilih Y (keluar dari program)
        clear_screen()
        exit(alert('INFO', 'Kamu telah keluar dari program!'))
    elif pilihan == 'T': # <-- Jika user memilih T (kembali ke inputan)
        clear_screen()
        alert('INFO', 'Kamu telah kembali ke inputan!')
        pause_program()
    else:  # <-- Jika user memilih selain Y atau T
        clear_screen()
        alert('ERROR', 'Silahkan pilih Y atau T!')
        exit_program()