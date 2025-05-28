from Order import Order
from db import CURSOR

class OrderList:

    @staticmethod
    def list_all_orders():
        CURSOR.execute("SELECT * FROM orders")
        rows = CURSOR.fetchall()
        return [
            Order(id=row[0], user_id=row[1], pizza_id=row[2], quantity=row[3], completed=bool(row[4]))
            for row in rows
        ]
