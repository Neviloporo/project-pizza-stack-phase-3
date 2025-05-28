class Pizza:
    _id_counter = 1
    _menu = []

    def __init__(self, name, size, toppings, price):
        self.id = Pizza._id_counter
        self.name = name
        self.size = size
        self.toppings = toppings
        self.price = price
        Pizza._id_counter += 1
        Pizza._menu.append(self)

    def __repr__(self):
        toppings_str = ', '.join(self.toppings)
        return f"<Pizza {self.id}: {self.name} ({self.size}) - ${self.price:.2f} [{toppings_str}]>"
    
    def list_maenu(cls):
        return cls._menu.copy()
    
    def get_pizza_by_id(cls, pizza_id):
        return next((pizza for pizza in cls._menu if pizza.id == pizza_id), None)
    
    