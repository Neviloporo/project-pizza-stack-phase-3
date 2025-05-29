from db import CURSOR, CONN

class Pizza:
    def __init__(self, name, size, price, toppings=None, id=None):
        self.id = id
        self.name = name
        self.size = size
        self.price = price
        self.toppings = toppings or []

    def save(self):
        """Save the pizza to the database, updating if it already exists."""
        if self.id:
            CURSOR.execute("""
                UPDATE pizzas
                SET name = ?, size = ?, price = ?
                WHERE id = ?
            """, (self.name, self.size, self.price, self.id))
        else:
            CURSOR.execute("""
                INSERT INTO pizzas (name, size, price)
                VALUES (?, ?, ?)
            """, (self.name, self.size, self.price))
            self.id = CURSOR.lastrowid

        
        CURSOR.execute("DELETE FROM pizza_toppings WHERE pizza_id = ?", (self.id,))
        for topping in self.toppings:
            CURSOR.execute("INSERT INTO pizza_toppings (pizza_id, topping) VALUES (?, ?)", (self.id, topping))

        CONN.commit()

    
    def get_all(cls):
        """Return a list of all pizzas with their toppings."""
        CURSOR.execute("SELECT * FROM pizzas")
        rows = CURSOR.fetchall()
        pizzas = []

        for row in rows:
            pizza_id = row[0]
            CURSOR.execute("SELECT topping FROM pizza_toppings WHERE pizza_id = ?", (pizza_id,))
            toppings = [t[0] for t in CURSOR.fetchall()]
            pizzas.append(cls(id=pizza_id, name=row[1], size=row[2], price=row[3], toppings=toppings))

        return pizzas

    
    def find_by_id(cls, pizza_id):
        """Find a pizza by its ID."""
        CURSOR.execute("SELECT * FROM pizzas WHERE id = ?", (pizza_id,))
        row = CURSOR.fetchone()
        if row:
            CURSOR.execute("SELECT topping FROM pizza_toppings WHERE pizza_id = ?", (pizza_id,))
            toppings = [t[0] for t in CURSOR.fetchall()]
            return cls(id=row[0], name=row[1], size=row[2], price=row[3], toppings=toppings)
        return None

    def delete(self):
        """Delete the pizza and its toppings from the database."""
        if self.id:
            CURSOR.execute("DELETE FROM pizza_toppings WHERE pizza_id = ?", (self.id,))
            CURSOR.execute("DELETE FROM pizzas WHERE id = ?", (self.id,))
            CONN.commit()
            self.id = None

    def __repr__(self):
        return f"<Pizza id={self.id} name={self.name} size={self.size} price={self.price} toppings={self.toppings}>"
