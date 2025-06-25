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


def show_products() -> None:
    produtcs = get_products()

    if produtcs:
        print('-' * 60)
        print("All Products:\n")
        for product in produtcs:
            print_product(product)
        print('-' * 60)
    else:
        print("No Product.")

