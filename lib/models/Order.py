from User import User
from Pizza import Pizza

class Order:
    _id_counter = 1
    _orders = []

    def __init__(self, user, pizza, quantity):
        self.id = Order._id_counter
        self.user = user
        self.pizza = pizza
        self.quantity = quantity
        self.completed = False
        Order._id_counter += 1
        Order._orders.append(self)

    def __repr__(self):
        status = "Completed" if self.completed else "Pending"
        return (f"<Order {self.id}: {self.quantity}x {self.pizza.name} "
                f"for {self.user.name} - ${self.total_price():.2f} [{status}]>")
    
    def total_price(self):
        return self.pizza.price * self.quantity

    def mark_completed(self):
        self.completed = True

    def create_order(cls, user_id, pizza_id, quantity):
        user = User.get_user_by_id(user_id)
        pizza = Pizza.get_pizza_by_id(pizza_id)
        if not user:
            raise ValueError("Invalid user ID.")
        if not pizza:
            raise ValueError("Invalid pizza ID.")
        if quantity <= 0:
            raise ValueError("Quantity must be at least 1.")
        return cls(user, pizza, quantity)
    
    def get_order_by_id(cls, order_id):
        return next((order for order in cls._orders if order_id == order_id), None)
    
    def list_all_order(cls):
        return cls._orders.copy()
    
    def list_order_by_user(cls, user_id):
        return [order for order in cls._orders if order.user.id == user_id]