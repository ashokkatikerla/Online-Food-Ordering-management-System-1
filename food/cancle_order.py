def cancel_order():
    if len(cart) == 0:
        print("Cart Already Empty")
    else:
        cart.clear()
        print("Order Cancelled")