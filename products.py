from termcolor import colored
from db import get_products


template_product = """#{id} name: {name}
    price: {price}
    stock: {stock}
    description: {description}
"""

def print_product(product: dict) -> None:
    print(template_product.format(
        id=product['id'],
        name=product['name'],
        price=product['price'],
        stock=product['stock'],
        description=product['description']
    ))


def print_products(products: list[dict]) -> None:
    print('-' * 60)
    print("All Products:\n")
    for product in products:
        print_product(product)
    print('-' * 60)


def show_products() -> bool:
    products = get_products()

    if products:
        print_products(products)
        return True
    else:
        print("No Product.")
        return False


def filter_menu() -> None:
    print("""
    === Filter Menu ===
    1. Get Products By Name
    2. Get Products By ID
    3. Get Products Greater Than Price
    4. Get Products Lass Than Price
    5. Get Products Greater In Range
    6. Back
    """)


def get_products_by_name() -> None:
    name = input("Search: ")

    products = get_products()

    filtered_prodcuts = filter(
        lambda product: name.lower() in product['name'].lower(),
        products
    )

    if filter_products:
        print_products(list(filtered_prodcuts))
    else:
        print("No Products.")


def get_products_by_id() -> None:
    id = int(input("ID: "))

    products = get_products()

    filtered_prodcuts = filter(
        lambda product: id == product['id'],
        products
    )

    if filter_products:
        print_products(list(filtered_prodcuts))
    else:
        print("No Products.")


def get_products_greater_than() -> None:
    price = float(input("min price: "))

    products = get_products()

    filtered_prodcuts = filter(
        lambda product: price <= product['price'],
        products
    )

    if filter_products:
        print_products(list(filtered_prodcuts))
    else:
        print("No Products.")


def get_products_less_than() -> None:
    price = float(input("max price: "))

    products = get_products()

    filtered_prodcuts = filter(
        lambda product: price >= product['price'],
        products
    )

    if filter_products:
        print_products(list(filtered_prodcuts))
    else:
        print("No Products.")


def get_products_in() -> None:
    min_price = float(input("min price: "))
    max_price = float(input("max price: "))

    products = get_products()

    filtered_prodcuts = filter(
        lambda product: min_price <= product['price'] <= max_price,
        products
    )

    if filter_products:
        print_products(list(filtered_prodcuts))
    else:
        print("No Products.")


def filter_products() -> None:
    if show_products():
        while True:
            filter_menu()
            choice = input("Menu Tanlang: ")

            if choice == '1':
                get_products_by_name()
            elif choice == '2':
                get_products_by_id()
            elif choice == '3':
                get_products_greater_than()
            elif choice == '4':
                get_products_less_than()
            elif choice == '5':
                get_products_in()
            elif choice == '6':
                break
            else:
                colored_text = colored("Bunday Menu Mavjud Emas!", "red")
                print(colored_text)
        

