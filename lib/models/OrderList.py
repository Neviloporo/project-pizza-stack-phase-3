from Order import Order  

class OrderList:
    @staticmethod
    def list_all_orders():
        """Return a list of all orders."""
        return Order.get_all()

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
