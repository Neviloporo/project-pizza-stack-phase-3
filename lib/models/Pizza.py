from db import CURSOR, CONN
import json

class Pizza:
    def __init__(self, name, size, toppings, price, id=None):
        self.id = id
        self.name = name
        self.size = size
        self.toppings = toppings  # list
        self.price = price

    def save(self):
        toppings_str = json.dumps(self.toppings)
        if self.id:
            CURSOR.execute(
                "UPDATE pizzas SET name = ?, size = ?, toppings = ?, price = ? WHERE id = ?",
                (self.name, self.size, toppings_str, self.price, self.id)
            )
        else:
            CURSOR.execute(
                "INSERT INTO pizzas (name, size, toppings, price) VALUES (?, ?, ?, ?)",
                (self.name, self.size, toppings_str, self.price)
            )
            self.id = CURSOR.lastrowid
        CONN.commit()

    @classmethod
    def get_by_id(cls, id):
        CURSOR.execute("SELECT * FROM pizzas WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls(id=row[0], name=row[1], size=row[2], toppings=json.loads(row[3]), price=row[4]) if row else None

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM pizzas")
        return [
            cls(id=row[0], name=row[1], size=row[2], toppings=json.loads(row[3]), price=row[4])
            for row in CURSOR.fetchall()
        ]

    def delete(self):
        if self.id:
            CURSOR.execute("DELETE FROM pizzas WHERE id = ?", (self.id,))
            CONN.commit()
