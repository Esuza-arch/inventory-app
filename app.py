import os
import sys
sys.path.append("/home/odiara/Development/code/phase-3/inventory-app")


from lib.db.database import create_conn
from lib.models.user import User
from lib.models.product import Product
from lib.models.category import Category

def main_menu():
    print("Welcome to the Inventory Management System")
    while True:
        print("\nMain Menu:")
        print("1. Manage Users")
        print("2. Manage Products")
        print("3. Manage Categories")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manage_users()
        elif choice == '2':
            manage_products()
        elif choice == '3':
            manage_categories()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_users():
    while True:
        print("\nManage Users:")
        print("1. Add User")
        print("2. Delete User")
        print("3. View All Users")
        print("4. Find User by ID")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            user = User.create(name=name, email=email)
            print(f"User {user[1]} created with ID {user[0]}.")
        elif choice == '2':
            user_id = int(input("Enter user ID to delete: "))
            if User.delete(user_id):
                print(f"User with ID {user_id} deleted.")
            else:
                print("User not found.")
        elif choice == '3':
            users = User.get_all()
            print("\nUsers:")
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to find: "))
            user = User.find_by_id(user_id)
            if user:
                print(user)
            else:
                print("User not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_products():
    while True:
        print("\nManage Products:")
        print("1. Add Product")
        print("2. Delete Product")
        print("3. View All Products")
        print("4. Find Product by ID")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            category_id = int(input("Enter category ID: "))
            product = Product.create(name=name, price=price, category_id=category_id)
            print(f"Product {product[1]} created with ID {product[0]}.")
        elif choice == '2':
            product_id = int(input("Enter product ID to delete: "))
            if Product.delete(product_id):
                print(f"Product with ID {product_id} deleted.")
            else:
                print("Product not found.")
        elif choice == '3':
            products = Product.get_all()
            print("\nProducts:")
            for product in products:
                print(product)
        elif choice == '4':
            product_id = int(input("Enter product ID to find: "))
            product = Product.find_by_id(product_id)
            if product:
                print(product)
            else:
                print("Product not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_categories():
    while True:
        print("\nManage Categories:")
        print("1. Add Category")
        print("2. Delete Category")
        print("3. View All Categories")
        print("4. Find Category by ID")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter category name: ")
            category = Category.create(name=name)
            print(f"Category {category[1]} created with ID {category[0]}.")
        elif choice == '2':
            category_id = int(input("Enter category ID to delete: "))
            if Category.delete(category_id):
                print(f"Category with ID {category_id} deleted.")
            else:
                print("Category not found.")
        elif choice == '3':
            categories = Category.get_all()
            print("\nCategories:")
            for category in categories:
                print(category)
        elif choice == '4':
            category_id = int(input("Enter category ID to find: "))
            category = Category.find_by_id(category_id)
            if category:
                print(category)
            else:
                print("Category not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    with create_conn() as conn:
        cursor = conn.cursor()
        User.create_table(cursor)
        Product.create_table(cursor)
        Category.create_table(cursor)
        conn.commit()
    main_menu()    