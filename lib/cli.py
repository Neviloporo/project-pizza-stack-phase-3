from lib.models.User import User
from lib.models.Pizza import Pizza
from lib.models.Order import Order
from lib.models.OrderList import OrderList
from .helpers import get_input

def display_users():
    users = User.get_all()
    if users:
        print("\nUsers:")
        for user in users:
            print(f"  {user.id}: {user.name} ({user.email})")
    else:
        print("No users found.")

def display_pizzas():
    pizzas = Pizza.get_all()
    if pizzas:
        print("\nPizzas:")
        for pizza in pizzas:
            toppings = ', '.join(pizza.toppings) if pizza.toppings else "None"
            print(f"  {pizza.id}: {pizza.name} - {pizza.size} - ${pizza.price:.2f} | Toppings: {toppings}")
    else:
        print("No pizzas available.")

def display_orders():
    orders = OrderList.list_all_orders()
    if orders:
        print("\nOrders:")
        for o in orders:
            status = "Completed" if o.completed else "Pending"
            print(f"  Order {o.id}: User #{o.user_id} - Pizza #{o.pizza_id} x{o.quantity} - {status}")
    else:
        print("No orders found.")

def add_pizza():
    name = input("Pizza name: ")
    size = input("Size (Small/Medium/Large): ")
    price = float(input("Price: "))
    toppings = input("Toppings (comma-separated): ").split(",")

    
    toppings = [t.strip() for t in toppings if t.strip()]

    pizza = Pizza(name=name, size=size, price=price, toppings=toppings)
    pizza.save()
    print(f"Pizza '{pizza.name}' added successfully!")


def place_order():
    display_users()
    user_id = get_input("Enter User ID: ", cast=int)
    if not User.find_by_id(user_id):
        print("Invalid User ID.")
        return

    display_pizzas()
    pizza_id = get_input("Enter Pizza ID: ", cast=int)
    if not Pizza.find_by_id(pizza_id):
        print("Invalid Pizza ID.")
        return

    quantity = get_input("Enter quantity: ", cast=int)

    try:
        order = Order(user_id=user_id, pizza_id=pizza_id, quantity=quantity)
        order.save()
        print("Order placed successfully!")
    except Exception as e:
        print("Error placing order:", e)

def add_user():
    name = input("Enter user's name: ")
    email = input("Enter user's email: ")

    if User.find_by_email(email):
        print("A user with this email already exists.")
        return

    user = User(name=name, email=email)
    user.save()
    print(f"User '{user.name}' added successfully!")

def remove_order():
    display_orders()
    order_id = input("Enter Order ID to delete: ").strip()

    try:
        order_id = int(order_id)
        order = OrderList.find_order_by_id(order_id)
        if order:
            order.delete()
        else:
            print("Order not found.")
    except ValueError:
        print("Invalid input. Please enter a valid Order ID.")

def menu():
    options = {
        "1": ("View all users", display_users),
        "2": ("View all pizzas", display_pizzas),
        "3": ("Place an order", place_order),
        "4": ("View all orders", display_orders),
        "5": ("Add new pizza", add_pizza),
        "6": ("Add new user", add_user),
        "7": ("Remove an order", remove_order),
        "8": ("Exit", None),
    }

    while True:
        print("\nPizza Stack CLI Menu")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")

        choice = input("Choose an option: ").strip()

        if choice in options:
            action = options[choice][1]
            if action:
                action()
            else:
                print("Goodbye!")
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
