## 🛒 E-Commerce CLI (Python)

### 📌 Description

This is a simple **Command Line E-commerce Application** written in Python.
Users can:

* Add new products
* View product catalog
* Make orders
* View all orders

This app runs entirely in the **terminal (CLI)** and uses in-memory storage (no database required).

---

### 🛠️ Features

* 🧾 Add new products with name, price, and quantity
* 📦 Show product list
* 🛍️ Place orders (based on available quantity)
* 📑 View all orders made during the session

---

### 🚀 How to Run

#### 1. Clone this repository

```bash
git clone https://github.com/yourusername/ecommerce-cli.git
cd ecommerce-cli
```

#### 2. Run the script

```bash
python ecommerce.py
```

> ⚠️ Make sure you have **Python 3.6+** installed on your machine.

---

### 🧪 Example Menu

```text
========= E-Commerce CLI =========
1. Add Product
2. View Products
3. Make Order
4. View Orders
5. Exit
==================================
```

---

### 📂 Project Structure

```
ecommerce-cli/
├── ecommerce.py      # Main application
├── README.md         # Project documentation
```

---

### 📌 Example Code Snippet

```python
products = []
orders = []

def add_product():
    name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    products.append({"name": name, "price": price, "quantity": quantity})
```

---

### 💡 Ideas for Improvement

* Store products and orders in a JSON file or SQLite database
* Add user registration and login
* Apply discounts or promo codes
* Export orders to CSV

---

### 📄 License

This project is open-source and free to use.

---
