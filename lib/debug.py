from lib.models.User import User
from lib.models.Pizza import Pizza
from lib.models.Order import Order
import code

if __name__ == "__main__":
    users = User.get_all()
    pizzas = Pizza.get_all()
    orders = Order.get_all()

    print("\nPizza Stack Debug Shell")
    print(f"🔹 {len(users)} users loaded into `users`")
    print(f"🔹 {len(pizzas)} pizzas loaded into `pizzas`")
    print(f"🔹 {len(orders)} orders loaded into `orders`")
    print("\nYou can also use User, Pizza, and Order classes directly.")

    
    print("Try `User.get_all()`, `Pizza.find_by_id(id)`, etc.")

    code.interact(local=locals())
