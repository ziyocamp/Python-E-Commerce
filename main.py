from termcolor import colored
from users import register, login


def show_menu() -> None:
    print("""
    === Menu ===
    1. Kirish
    2. Royxatdan O'tish
    3. Barcha Mahsulotlarni Ko'rish
    4. Mahsulotlarni Filter Qilish
    5. Buyurtma Berish
    6. Chiqish
    """)


def main() -> None:
    while True:
        show_menu()
        choice = input("Menu Tanlang: ")

        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        else:
            colored_text = colored("Bunday Menu Mavjud Emas!", "red")
            print(colored_text)


if __name__ == "__main__":
    main()
