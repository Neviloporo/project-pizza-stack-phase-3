from db import CONN, CURSOR

class Order:
    def __init__(self, user_id, pizza_id, quantity, completed=False, id=None):
        self.id = id
        self.user_id = user_id
        self.pizza_id = pizza_id
        self.quantity = quantity
        self.completed = completed

    def save(self):
        if self.id:
            CURSOR.execute(
                "UPDATE orders SET user_id = ?, pizza_id = ?, quantity = ?, completed = ? WHERE id = ?",
                (self.user_id, self.pizza_id, self.quantity, int(self.completed), self.id)
            )
        else:
            CURSOR.execute(
                "INSERT INTO orders (user_id, pizza_id, quantity, completed) VALUES (?, ?, ?, ?)",
                (self.user_id, self.pizza_id, self.quantity, int(self.completed))
            )
            self.id = CURSOR.lastrowid
        CONN.commit()

    @classmethod
    def get_by_id(cls, id):
        CURSOR.execute("SELECT * FROM orders WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls(id=row[0], user_id=row[1], pizza_id=row[2], quantity=row[3], completed=bool(row[4])) if row else None

    def mark_completed(self):
        self.completed = True
        self.save()

    def delete(self):
        if self.id:
            CURSOR.execute("DELETE FROM orders WHERE id = ?", (self.id,))
            CONN.commit()
