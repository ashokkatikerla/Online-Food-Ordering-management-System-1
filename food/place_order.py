def place_order():
    if len(cart) == 0:
        print("Cart is Empty")
        return
    total = 0
    for item in cart:
        total += item[1]
    print("Order Placed Successfully")
    print("Total Bill = Rs.", total)
    cart.clear()