import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def alert(title, message):
    print(f'-- {title} {27 * "-"}')
    print(f"{message}")
    print('-' * 35)

def pause():
    input('\n>> Tekan ENTER untuk melanjutkan <<')

def exitProgram():
    pilihan = input("Apakah kamu yakin akan keluar dari program? [Y/T]: ").upper()

    if pilihan == 'Y':
        clear()
        exit(
            alert('INFO', 'Kamu telah keluar dari program!')
        )
    elif pilihan == 'T':
        clear()
        alert('INFO', 'Kamu telah kembali ke inputan!')
        pause()
    else: 
        clear()
        alert('ERROR', 'Silahkan pilih Y atau T!')
        exitProgram()