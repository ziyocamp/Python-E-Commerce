from termcolor import colored
from db import add_user


def register() -> None:
    colored_text = colored("Ro'yxatdan o'tish uchun ma'lumotlaringizni kiriting:", "yellow")
    print(colored_text)

    first_name = input("Ismingiz: ")
    last_name = input("Familiyangiz: ")
    birth_year = input("tug'gilgan yilingiz: ")
    email = input("Elektron pochtangiz: ")

    checkings = []
    checkings.append(first_name.isalpha())
    checkings.append(last_name.isalpha())
    checkings.append(birth_year.isdigit())
    checkings.append("@" in email)

    if not all(checkings):
        colored_text = colored("Noto'g'ri malumot kiritdingiz.", "red")
        print(colored_text)
        return 

    result = add_user(
        first_name,
        last_name,
        int(birth_year),
        email
    )

    if result:
        colored_text = colored("Muvaffaqiyatli ro'yxatdan o'tdingiz.", "green")
        print(colored_text)
    else:
        colored_text = colored("Ro'yxatdan o'tishga xatolik yuz berdi.", "red")
        print(colored_text)
