from tabulate import tabulate 
import apps.action as action
from apps.infix import InfixConverter as infix
from apps.prefix import PrefixConverter as prefix
from apps.postfix import PostfixConverter as postfix

if __name__ == '__main__':
    while True:
        action.clear()
        action.alert(None, "Silahkan pilih menu yang tersedia!")

        print(
            tabulate(
                [
                    ["Kode", "Nama Menu"],
                    ["0", "Keluar dari Menu"], 
                    ["1", "Konversi INFIX => Postfix & Prefix"],
                    ["2", "Konversi PREFIX => Infix & Postfix"],
                    ["3", "Konversi POSTFIX => Infix & Prefix"],
                ],
                headers='firstrow', 
                tablefmt='grid' 
            )
        )

        print('-' * 40)
        choice = input("Pilih Kode Menunya: ")
        print('-' * 40)

        if not choice.isdigit():
            action.clear()
            action.alert('ERROR', 'Silahkan pilih kode yang tersedia!')
            action.pause()
        elif choice == '0':
            action.clear()
            action.exitProgram()
        elif choice == '1':
            action.clear()
            infix.convert()
        elif choice == '2':
            action.clear()
            prefix.convert()
        elif choice == '3':
            action.clear()
            postfix.convert()
        else:
            action.clear()
            action.alert('ERROR', 'Silahkan pilih kode yang tersedia!')
            action.pause()