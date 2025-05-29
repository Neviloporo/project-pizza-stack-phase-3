from lib.db import CURSOR, CONN

class Order:
    def __init__(self, user_id, pizza_id, quantity=1, completed=False, id=None):
        self.id = id
        self.user_id = user_id
        self.pizza_id = pizza_id
        self.quantity = quantity
        self.completed = completed

    def save(self):
        """Insert a new order or update an existing one in the database."""
        if self.id:
            CURSOR.execute("""
                UPDATE orders
                SET user_id = ?, pizza_id = ?, quantity = ?, completed = ?
                WHERE id = ?
            """, (self.user_id, self.pizza_id, self.quantity, int(self.completed), self.id))
        else:
            CURSOR.execute("""
                INSERT INTO orders (user_id, pizza_id, quantity, completed)
                VALUES (?, ?, ?, ?)
            """, (self.user_id, self.pizza_id, self.quantity, int(self.completed)))
            self.id = CURSOR.lastrowid
        CONN.commit()

    def delete(self):
        if self.id:
            CURSOR.execute("DELETE FROM orders WHERE id = ?", (self.id,))
            CONN.commit()
            print(f"Order #{self.id} has been deleted.")
            self.id = None

    @classmethod
    def get_all(cls):
        """Return a list of all Order instances from the database."""
        CURSOR.execute("SELECT * FROM orders")
        rows = CURSOR.fetchall()
        return [cls(id=row[0], user_id=row[1], pizza_id=row[2], quantity=row[3], completed=bool(row[4])) for row in rows]

    def __repr__(self):
        return (f"<Order id={self.id} user_id={self.user_id} pizza_id={self.pizza_id} "
                f"quantity={self.quantity} completed={self.completed}>")
