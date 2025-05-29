from lib.db import CURSOR, CONN
from lib.models.Order import Order

class OrderList:
    @classmethod
    def list_all_orders(cls):
        CURSOR.execute("SELECT * FROM orders")
        rows = CURSOR.fetchall()
        return [
            Order(id=row[0], user_id=row[1], pizza_id=row[2], quantity=row[3], completed=bool(row[4]))
            for row in rows
        ]

    @staticmethod
    def list_pending_orders():
        """Return a list of orders that are not yet completed."""
        return [order for order in Order.get_all() if not order.completed]

    @staticmethod
    def list_completed_orders():
        """Return a list of orders that have been completed."""
        return [order for order in Order.get_all() if order.completed]

    @staticmethod
    def list_orders_by_user(user_id):
        """Return all orders for a given user ID."""
        return [order for order in Order.get_all() if order.user_id == user_id]
    
    @classmethod
    def find_order_by_id(cls, order_id):
        CURSOR.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
        row = CURSOR.fetchone()
        if row:
            return Order(id=row[0], user_id=row[1], pizza_id=row[2], quantity=row[3], completed=bool(row[4]))
        return None

    @classmethod
    def delete_order(cls, order_id):
        CURSOR.execute("DELETE FROM orders WHERE id = ?", (order_id,))
        CONN.commit()
