from Order import Order

class OrderList:
    
    def list_all_orders():
        return Order.list_all_orders()
    
    def list_pending_orders():
        return [order for order in Order.List_all_orders() if not order.completed]
    
    def list_completed_orders():
        return [order for order in Order.list_all_order() if order.completed]
    
    def list_orders_by_user(user_id):
        return Order.list_orders_by_user(user_id)
    
    def mark_order_completed(order_id):
        order = Order.get_order_by_id(order_id)
        if order:
            order.mark_completed()
            return True
        return False
    
    def get_order_by_id(order_id):
        return Order.get_order_by_id(order_id)