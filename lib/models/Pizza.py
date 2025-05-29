from lib.db import CURSOR, CONN

class Pizza:
    def __init__(self, name, size, price, toppings=None, id=None):
        self.id = id
        self.name = name
        self.size = size
        self.price = price
        self.toppings = toppings or []

    def __repr__(self):
        return f"<Pizza {self.id}: {self.name}, {self.size}, ${self.price:.2f} | Toppings: {', '.join(self.toppings)}>"

    def save(self):
        if self.id:
            CURSOR.execute("""
                UPDATE pizzas SET name=?, size=?, price=? WHERE id=?
            """, (self.name, self.size, self.price, self.id))
        else:
            CURSOR.execute("""
                INSERT INTO pizzas (name, size, price) VALUES (?, ?, ?)
            """, (self.name, self.size, self.price))
            self.id = CURSOR.lastrowid
        CURSOR.execute("DELETE FROM pizza_toppings WHERE pizza_id = ?", (self.id,))
        for topping in self.toppings:
            CURSOR.execute("""
                INSERT INTO pizza_toppings (pizza_id, topping) VALUES (?, ?)
            """, (self.id, topping))
        CONN.commit()

    def delete(self):
        if self.id:
            CURSOR.execute("DELETE FROM pizza_toppings WHERE pizza_id = ?", (self.id,))
            CURSOR.execute("DELETE FROM pizzas WHERE id = ?", (self.id,))
            CONN.commit()

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM pizzas")
        rows = CURSOR.fetchall()
        pizzas = []
        for row in rows:
            pizza_id, name, size, price = row
            CURSOR.execute("SELECT topping FROM pizza_toppings WHERE pizza_id = ?", (pizza_id,))
            toppings = [t[0] for t in CURSOR.fetchall()]
            pizzas.append(Pizza(name, size, price, toppings, pizza_id))
        return pizzas
    
    @classmethod
    def find_by_name_size_price(cls, name, size, price):
        CURSOR.execute("""
        SELECT id FROM pizzas WHERE LOWER(name) = LOWER(?) AND LOWER(size) = LOWER(?) AND price = ?
        """, (name, size, price))
        row = CURSOR.fetchone()
        return bool(row)


    def __eq__(self, other):
        return (
            isinstance(other, Pizza) and
            self.name.lower() == other.name.lower() and
            self.size.lower() == other.size.lower() and
            float(self.price) == float(other.price) and
            sorted(t.lower() for t in self.toppings) == sorted(t.lower() for t in other.toppings)
        )
